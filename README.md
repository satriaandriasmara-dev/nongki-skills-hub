# nongki-skills-hub

Curated [Claude Code](https://claude.com/product/claude-code) skills — versioned, reusable, and warung-tested.

This repo is the **source of truth** for the skills installed via `~/.claude/skills/` (symlinked). Edit here, take effect everywhere.

## Skills

| Skill | Purpose | Tags |
|---|---|---|
| [changes-committing](skills/changes-committing/) | Secure git commits: credential scanning, file filtering, conventional commit messages, no secrets ever land in history | `git` `security` `conventional-commits` |
| [eyd-indonesia](skills/eyd-indonesia/) | Indonesian proofreading & editing according to official EYD V (spelling, capitalization, punctuation, loanwords) | `indonesian` `eyd` `proofreading` |
| [humanizer-indonesia](skills/humanizer-indonesia/) | Rewrite Indonesian text to sound natural, human, and contextually appropriate without changing original meaning | `indonesian` `humanizer` `naturalize` |
| [laporan-pengawasan-bpkp](skills/laporan-pengawasan-bpkp/) | Draft, edit, and review BPKP internal audit reports (LHP/LHE/LHR) following Peraturan BPKP No. 4/2026 and IIA Global Standards; includes Python engine for automated Word (.docx) generation with multilevel numbering cascade (`A. → 1. → a. → 1)`), native Heading styles (Arial 12pt bold), 3/2/2/2.5 cm margins (left/right/top/bottom, Perban 4/2026 minimums), hanging indents, and 1.15 line pitch | `bpkp` `audit` `laporan` `5c` `iia` `peraturan-bpkp-4-2026` `docx` |
| [tata-naskah-dinas-bpkp](skills/tata-naskah-dinas-bpkp/) | Compose, edit, and validate BPKP official naskah dinas (surat dinas, nota dinas, surat tugas, etc.) per Peraturan BPKP No. 4/2026; includes Python helpers for kop surat, nota dinas, surat tugas, lembar pengesahan, heading styles, and TTE | `bpkp` `tata-naskah-dinas` `naskah-dinas` `peraturan-bpkp-4-2026` `docx` |
| [mpp-bpkp](skills/mpp-bpkp/) | Generate full BPKP audit planning packages (MPP / Manajemen Penugasan Pengawasan) and Surat Tugas preparation per Peraturan BPKP No. 2/2023 and No. 4/2026; fills 11–12 official DOCX templates, automates Word PDF rendering and merged preview, and includes a streamlined Excel master for flexible team assignment (up to 20 members) without private data | `bpkp` `mpp` `surat-tugas` `audit-planning` `peraturan-bpkp-2-2023` `peraturan-bpkp-4-2026` `docx` |
| [pdf-comprehension](skills/pdf-comprehension/) | Deep PDF analysis: extracts pages as images, reads them visually, produces structured markdown summaries with visual highlights | `pdf` `analysis` `document` |
| [study-guide-writing](skills/study-guide-writing/) | Manning/No Starch Press-style study guides from source materials — LaTeX to PDF + EPUB, with note/tip/warning boxes and war stories | `latex` `pdf` `epub` `education` |
| [tsundere-code-style](skills/tsundere-code-style/) | Write code as if authored by a tsundere programmer — playful sentence-like names, booleans, functions, comments, and error messages that stay functional and understandable | `code-style` `fun` `naming` `humor` |
| [image-generation](skills/image-generation/) | Generate images via any OpenAI-compatible Images API (OpenRouter, OmniRoute, LiteLLM, …) — env-configured endpoint/key/model, with hand-authored SVG fallback | `image-generation` `openai-compatible` `api` |
| [vault-notetaking](skills/vault-notetaking/) | Capture durable learnings into an Obsidian second brain (PARA-style), configurable via `VAULT_DIR` | `obsidian` `second-brain` `knowledge-management` |

Some skills need a little environment configuration:

```bash
# image-generation — any OpenAI-compatible Images API endpoint
export IMAGE_API_BASE="https://openrouter.ai/api"   # no trailing /v1
export IMAGE_API_KEY="your_key"
export IMAGE_API_MODEL="google/gemini-2.5-flash-image"   # optional

# vault-notetaking — where your Obsidian vault lives
export VAULT_DIR="$HOME/your-vault"
```

## Install

### From this repo (fresh machine / another environment)

```bash
git clone git@github.com:septiannugraha/nongki-skills-hub.git ~/code/nongki-skills-hub

# Claude Code
mkdir -p ~/.claude/skills
for skill in ~/code/nongki-skills-hub/skills/*/; do
  ln -sfn "$skill" ~/.claude/skills/"$(basename "$skill")"
done

# Antigravity / Agents
mkdir -p ~/.agents/skills
for skill in ~/code/nongki-skills-hub/skills/*/; do
  ln -sfn "$skill" ~/.agents/skills/"$(basename "$skill")"
done

# opencode
mkdir -p ~/.config/opencode/skills
for skill in ~/code/nongki-skills-hub/skills/*/; do
  ln -sfn "$skill" ~/.config/opencode/skills/"$(basename "$skill")"
done
```

Or cherry-pick only the skills you want:

```bash
ln -sfn ~/code/nongki-skills-hub/skills/changes-committing ~/.claude/skills/changes-committing
```

### Adding a new skill

1. `mkdir skills/<skill-name> && $EDITOR skills/<skill-name>/SKILL.md`
2. Follow the SKILL.md format: YAML frontmatter (`name`, `description`, `tags`), then the instructions.
3. `ln -sfn ~/code/nongki-skills-hub/skills/<skill-name> ~/.claude/skills/<skill-name>`
4. Commit and push. New machine? Run the install loop above and you're synced.

## Structure

```
nongki-skills-hub/
├── README.md
├── .gitignore
└── skills/
    ├── changes-committing/
    │   └── SKILL.md
    ├── eyd-indonesia/
    │   ├── SKILL.md
    │   ├── agents/
    │   └── references/
    ├── humanizer-indonesia/
    │   ├── SKILL.md
    │   ├── agents/
    │   └── references/
    ├── image-generation/
    │   ├── SKILL.md
    │   └── generate_image.py
    ├── laporan-pengawasan-bpkp/
    │   ├── SKILL.md
    │   ├── assets/            # BPKP logo (PNG + JPG), unit_profiles.json
    │   ├── references/
    │   └── scripts/           # bpkp_docx_engine.py, lhp_builder.py
    ├── tata-naskah-dinas-bpkp/
    │   ├── SKILL.md
    │   ├── assets/            # BPKP logo, unit_profiles.json, templates/ (46 master DOCX)
    │   ├── references/        # incl. templates_registry.json
    │   └── scripts/           # generate_naskah.py, naskah_dinas_helper.py, test_engine.py
    ├── mpp-bpkp/
    │   ├── SKILL.md
    │   ├── PANDUAN_PENGGUNAAN.md
    │   ├── README.md
    │   ├── agents/            # openai.yaml interface definition
    │   ├── assets/            # Isian_DATA_MPP_BPKP.xlsx, templates/ (12 master DOCX)
    │   ├── examples/          # Synthetic test datasets (PIA & Evaluasi)
    │   ├── references/        # Format specs, TND alignment & risk/KM-6 guides
    │   └── scripts/           # generate_mpp.py, model.py, create_workbook.py, verify_workflow.py
    ├── pdf-comprehension/
    │   └── SKILL.md
    ├── study-guide-writing/
    │   └── SKILL.md
    ├── tsundere-code-style/
    │   └── SKILL.md
    └── vault-notetaking/
        └── SKILL.md
```

## Curation policy

Skills in this hub are curated — battle-tested, generic enough to be useful across projects, and documented. Skills that are personal, machine-specific, or "creative" stay in `~/.claude/skills/` directly, outside this repo.

One hub serves **Claude Code** (`~/.claude/skills/`), **Antigravity** (`~/.agents/skills/`), and **opencode** (`~/.config/opencode/skills/`) via symlinks, so a skill improvement lands in all tools at once.

## License

Personal toolkit — no license for now. Flip to private-only or add one later if this ever goes public.
