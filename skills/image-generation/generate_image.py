#!/usr/bin/env python3
"""
Generate images through any OpenAI-compatible /v1/images/generations endpoint.

Works with OpenRouter, OmniRoute, LiteLLM, llamacpp, or a raw provider API —
anything that speaks the OpenAI Images API. All configuration comes from the
environment or flags, so the script works for any user without edits:

    IMAGE_API_BASE    Base URL, e.g. https://openrouter.ai/api  (no trailing /v1)
    IMAGE_API_KEY     API key (sent as Authorization: Bearer <key>)
    IMAGE_API_MODEL   Model id (default: google/gemini-2.5-flash-image)

Usage:
    python generate_image.py "a single red apple on a white background"
    python generate_image.py "prompt..." --out ./pictures/myimage
    python generate_image.py "prompt..." --base https://openrouter.ai/api --model google/gemini-2.5-flash-image
    python generate_image.py "prompt..." --size 1024x1024 --n 2

Requires:
    pip install requests
"""
import argparse
import base64
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' is required. Install it with: pip install requests", file=sys.stderr)
    sys.exit(1)

DEFAULT_BASE = os.environ.get("IMAGE_API_BASE", "").rstrip("/")
DEFAULT_MODEL = os.environ.get("IMAGE_API_MODEL", "google/gemini-2.5-flash-image")
DEFAULT_OUT_DIR = Path.cwd() / "images"
DEFAULT_SIZE = "1024x1024"


def slugify(text: str, max_len: int = 40) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:max_len].strip("-") or "image"


def sniff_extension(data: bytes) -> str:
    if data.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if data.startswith(b"\x89PNG"):
        return "png"
    if data.startswith(b"GIF8"):
        return "gif"
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return "webp"
    return "png"


def fire(prompt: str, base: str, model: str = DEFAULT_MODEL,
         size: str = DEFAULT_SIZE, n: int = 1,
         response_format: str = "b64_json") -> dict:
    if not base:
        raise RuntimeError(
            "No API base URL configured. Set IMAGE_API_BASE (e.g. "
            "https://openrouter.ai/api) or pass --base."
        )
    api_key = os.environ.get("IMAGE_API_KEY")
    headers = {"content-type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    payload = {
        "model": model,
        "prompt": prompt,
        "n": n,
        "size": size,
        "response_format": response_format,
    }
    t0 = time.time()
    r = requests.post(f"{base}/v1/images/generations", headers=headers,
                      json=payload, timeout=300)
    elapsed = time.time() - t0
    if not r.ok:
        raise RuntimeError(f"HTTP {r.status_code}\n{r.text[:1500]}")
    return {"elapsed_s": round(elapsed, 2), **r.json()}


def extract_item(item: dict) -> tuple[bytes, str]:
    if item.get("b64_json"):
        raw = base64.b64decode(item["b64_json"])
    elif item.get("base64"):
        raw = base64.b64decode(item["base64"])
    elif item.get("url"):
        resp = requests.get(item["url"], timeout=120)
        resp.raise_for_status()
        raw = resp.content
    elif item.get("image"):
        s = item["image"]
        if s.startswith("data:"):
            s = s.split(",", 1)[1]
        raw = base64.b64decode(s)
    else:
        raise RuntimeError(f"Unrecognized image item fields: {list(item)}")
    return raw, sniff_extension(raw[:16])


def save(result: dict, prompt: str, out_path: Path | None) -> list[Path]:
    data = result.get("data", [])
    if not data:
        raise RuntimeError(
            "No images returned. Check IMAGE_API_KEY and the model id."
        )

    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    saved = []
    multi = len(data) > 1

    for i, item in enumerate(data):
        img_bytes, ext = extract_item(item)
        if out_path is None:
            DEFAULT_OUT_DIR.mkdir(parents=True, exist_ok=True)
            name = f"generated_{slugify(prompt)}_{ts}"
            if multi:
                name += f"_{i}"
            path = DEFAULT_OUT_DIR / f"{name}.{ext}"
        else:
            base = Path(out_path)
            # with_suffix() rejects "_0.png" (suffix must start with "."), so build the
            # name explicitly; with --n > 1 every image gets its own index.
            stem, suffix = (base.stem, base.suffix) if base.suffix else (base.name, f".{ext}")
            path = base.with_name(f"{stem}_{i}{suffix}" if multi else f"{stem}{suffix}")
            path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(img_bytes)
        saved.append(path)

        revised = item.get("revised_prompt")
        if revised and not multi:
            sidecar = path.with_suffix(f".{ext}.revised.md")
            sidecar.write_text(f"Prompt: {prompt}\n\nRevised: {revised}\n", encoding="utf-8")

    return saved


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("prompt", help="Image generation prompt")
    p.add_argument("--out", type=Path, default=None,
                   help="Output path (default: ./images/auto-named)")
    p.add_argument("--base", default=DEFAULT_BASE,
                   help=f"API base URL without /v1 (default: $IMAGE_API_BASE; currently '{DEFAULT_BASE or 'unset'}')")
    p.add_argument("--model", default=DEFAULT_MODEL,
                   help=f"Model ID (default: {DEFAULT_MODEL}, or $IMAGE_API_MODEL)")
    p.add_argument("--size", default=DEFAULT_SIZE,
                   help=f"Image size (default: {DEFAULT_SIZE})")
    p.add_argument("--n", type=int, default=1, help="Number of images (default: 1)")
    p.add_argument("--response-format", default="b64_json",
                   choices=["b64_json", "url"],
                   help="Response format (default: b64_json)")
    args = p.parse_args()

    # Windows consoles/pipes often default to cp1252, which cannot print "→"/"✓".
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")

    # Accept "https://host/api/" or ".../v1" too; the endpoint path appends /v1 itself.
    args.base = re.sub(r"/v1$", "", args.base.rstrip("/"))

    if not args.base:
        print("ERROR: No API base URL configured. Set IMAGE_API_BASE (e.g. "
              "https://openrouter.ai/api) or pass --base.", file=sys.stderr)
        return 1

    print(f"→ Generating via {args.base}/v1/images/generations (model={args.model})")
    if os.environ.get("IMAGE_API_KEY"):
        print("  Auth: IMAGE_API_KEY (Bearer)")
    else:
        print("  Warning: IMAGE_API_KEY not set — generation may fail upstream")
    print(f"  Prompt: {args.prompt}")

    try:
        result = fire(args.prompt, args.base, model=args.model,
                      size=args.size, n=args.n,
                      response_format=args.response_format)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    try:
        saved = save(result, args.prompt, args.out)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(f"\n✓ {result['elapsed_s']}s")
    for path in saved:
        print(f"  {path.stat().st_size:,} bytes → {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
