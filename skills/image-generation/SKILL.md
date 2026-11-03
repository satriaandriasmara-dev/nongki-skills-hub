---
name: image-generation
description: Generate images via any OpenAI-compatible Images API endpoint (OpenRouter, OmniRoute, LiteLLM, direct provider). Configure with IMAGE_API_BASE, IMAGE_API_KEY, IMAGE_API_MODEL env vars. Use when user asks to generate or create an image, illustration, portrait, or cover art.
license: MIT
tags: [image-generation, openai-compatible, api, openrouter, litellm, media]
---

# Image Generation

Generate images from text prompts through **any OpenAI-compatible Images API** — OpenRouter, OmniRoute, LiteLLM proxy, or a provider's direct endpoint. The helper script lives **inside this skill directory**, so the skill is self-contained and portable.

## Script

```
<skill-dir>/generate_image.py
```

Plain Python CLI (requires `requests`; `pip install requests` if missing). It POSTs to `{base}/v1/images/generations` (OpenAI style) or, for `openrouter.ai`, to `{base}/v1/images` (OpenRouter's Image API), decodes the returned image, writes it to disk, and saves a `.revised.md` sidecar when the API returns a `revised_prompt`.

## Configuration

Everything is env-configurable — no hardcoded addresses, works for any user:

| Variable | Purpose | Example |
| --- | --- | --- |
| `IMAGE_API_BASE` | API base URL **without** `/v1` | `https://openrouter.ai/api` |
| `IMAGE_API_KEY` | API key, sent as `Authorization: Bearer <key>` | *(secret — keep in env, never in the skill)* |
| `IMAGE_API_MODEL` | Default model id | `google/gemini-2.5-flash-image` |
| `IMAGE_API_PATH` | Optional endpoint path override (default `/v1/images/generations`; `/v1/images` is picked automatically for `openrouter.ai`) | `/v1/images` |

Set them once in your shell profile (or `.env` + `direnv`) and every tool that loads this skill uses them:

```bash
export IMAGE_API_BASE="https://openrouter.ai/api"
export IMAGE_API_KEY="your_key_here"
export IMAGE_API_MODEL="google/gemini-2.5-flash-image"   # optional
```

## Usage

```bash
# Text-to-image using env configuration
python <skill-dir>/generate_image.py "a single red apple on a white background"

# Custom output path
python <skill-dir>/generate_image.py "prompt..." --out ./pictures/myimage

# Override endpoint or model ad hoc
python <skill-dir>/generate_image.py "prompt..." --base https://openrouter.ai/api --model google/gemini-2.5-flash-image

# Size and batch count
python <skill-dir>/generate_image.py "prompt..." --size 1024x1024 --n 2
```

## Options

| Flag | Description |
| --- | --- |
| `prompt` (positional) | The text prompt describing the image to generate |
| `--out PATH` | Output path; no extension defaults to the media type from the response |
| `--base URL` | API base URL without `/v1` (default: `$IMAGE_API_BASE`) |
| `--model ID` | Model ID (default: `$IMAGE_API_MODEL` or `google/gemini-2.5-flash-image`) |
| `--size WxH` | Image size (default `1024x1024`) |
| `--n N` | Number of images (default 1) |
| `--path PATH` | Endpoint path (default: `$IMAGE_API_PATH`, else auto as above) |
| `--response-format` | `b64_json` or `url`; not sent unless given, since some endpoints reject it (both response forms are handled) |

## Output

- Default output directory: `./images/` (relative to the current working directory; created automatically)
- Files: `generated_<prompt-slug>_<timestamp>.<ext>` plus a `<image>.<ext>.revised.md` sidecar when available
- The script prints the saved path, byte size, and elapsed time

## Workflow

1. Confirm what image the user wants
2. Verify `IMAGE_API_BASE` and `IMAGE_API_KEY` are set (the script warns if not)
3. Run the script with the bash tool, capturing the output path and elapsed time
4. If a model returns a capacity/quota error, retry with an alternative model via `--model`
5. If the endpoint is unreachable or every model fails, fall back to a hand-authored SVG (see below)
6. Report the saved image path and any `revised_prompt` sidecar

## SVG fallback

Only after real generation is exhausted — all alternative models tried, all failing — author an SVG by hand instead of leaving the user with nothing.

**Trigger conditions:**
- Endpoint unreachable (connection refused, DNS failure, timeout)
- Every alternative model returns an error (quota, capacity, auth, 5xx)
- `No images returned` persists across models

Do **not** fall back on the first error. Try alternative models first.

**How to author the fallback:**

1. Tell the user raster generation failed and that you're producing an SVG instead — never present it as if it came from the model
2. Write the SVG with the write tool to the same directory the raster image would have used (default `./images/`), named `<prompt-slug>_fallback.svg`
3. Use a `viewBox` matching the requested `--size` (default `0 0 1024 1024`) so it drops into the same layout
4. Build it from real vector primitives — paths, gradients, shapes composed into the actual subject. A rectangle with the prompt text in the middle is not a fallback, it's a placeholder; only degrade to that if the subject genuinely cannot be vectorized
5. Keep it self-contained: no external fonts, no linked assets, no embedded rasters
6. Save the prompt alongside it in a `<image>.revised.md` sidecar for parity with the normal path

**Suitability check.** SVG excels at flat, geometric, iconographic subjects — logos, diagrams, icons, simple scenes, silhouettes. It is a poor substitute for photorealism, complex texture, or detailed faces. When the request falls in that second category, produce the best vector interpretation you can *and* say plainly that it is a stylized stand-in, so the user can decide whether to retry later.

## Error handling

- `No API base URL configured`: `IMAGE_API_BASE` is unset and no `--base` given — set the env var or pass the flag
- `HTTP <status>` / connection errors: endpoint unreachable — verify the URL or pass `--base`. An `HTTP 404` usually means the endpoint path differs on this provider; set `IMAGE_API_PATH` / `--path`. If it stays unreachable, use the SVG fallback
- `No images returned`: usually means the upstream call failed — confirm `IMAGE_API_KEY` is set and the model id exists on the endpoint. If it persists across all models, use the SVG fallback
- Do not claim success without a real saved file; report the actual output of the script
- Never pass off a fallback SVG as model-generated output — always state which path produced the file
