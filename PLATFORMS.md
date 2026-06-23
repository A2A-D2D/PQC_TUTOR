# Multi-Platform Setup Guide — PQC Quickstart Tutor

This guide explains how to use the PQC Quickstart Tutor on various AI platforms.

## Quick Start (30 seconds)

The PQC Agent works out of the box on any platform that supports `AGENTS.md`:

1. **Clone/copy this repo** to your local machine
2. **Open the repo** in your AI tool
3. The tool automatically reads `AGENTS.md` and the database

The knowledge base (`database/`) is plain Markdown — **no API keys, no servers, no dependencies.**

---

## Platform-Specific Instructions

### ✅ Claude Code (Anthropic)

**Auto-detected.** Claude Code reads `CLAUDE.md` automatically when you open the repo.

```bash
cd PQC_Agent
claude
```

The full `CLAUDE.md` (~200 lines) includes extended teaching examples and interaction patterns.

---

### ✅ Claude Codex (Anthropic)

**Auto-detected.** Codex reads `AGENTS.md` from the repo root.

```bash
codex ./PQC_Agent
```

Works identically to Claude Code. The `AGENTS.md` provides a slightly more compact agent definition optimized for multi-platform compatibility.

---

### ✅ Cursor (Anyscale)

**Auto-detected.** Cursor reads `.cursor/rules/*.mdc` files.

1. Open the `PQC_Agent/` folder in Cursor
2. The `.cursor/rules/pqc-tutor.mdc` rule is set to `alwaysApply: true`
3. Use `Cmd+L` (Mac) or `Ctrl+L` (Windows) to chat with the PQC tutor

The rule is scoped to `**/*.md`, `**/*.pdf`, and `database/**/*` files.

---

### ✅ GitHub Copilot (Microsoft)

**Auto-detected.** Copilot reads `.github/copilot-instructions.md`.

1. Push this repo to GitHub
2. Open any file in VS Code with Copilot Chat
3. Use `@workspace` to reference the full knowledge base
4. Or ask: "Explain ML-KEM" — Copilot uses the instructions automatically

For best results, use Copilot Chat's **Ask** mode with `@workspace /explain`.

---

### ✅ Windsurf (Codeium)

**Auto-detected.** Windsurf reads `AGENTS.md`.

1. Open the `PQC_Agent/` folder in Windsurf
2. The agent context is automatically loaded
3. Use Cascade to ask PQC questions

---

### ✅ ChatGPT Custom GPT / Claude Project

For platforms that don't read files automatically, use the **Compact Prompt** from `AGENTS.md`:

1. Create a new Custom GPT or Claude Project
2. Upload key database files as "Knowledge" or "Project files":
   - `AGENTS.md`
   - `database/metadata/parameter_tables.md`
   - `database/metadata/parameter_tables_extended.md`
   - `database/metadata/standard_status.md`
   - `database/guides/algorithm_selection_guide.md`
   - `database/guides/cross_algorithm_comparison.md`
3. Paste this system prompt:

```
You are PQC Quickstart Tutor. Teach PQC to engineers who know RSA/ECC/AES.
Core rule: concepts OK, numbers MUST come from provided files.
NEVER invent parameters, sizes, status, or benchmarks.
Algorithm status: ML-KEM/ML-DSA/SLH-DSA=FIPS standard. Falcon/HQC=future std. Others=candidates/research.
Use traditional-crypto analogies. Label analogies clearly.
Always say "not in database" rather than guessing.
```

---

### ✅ Any other AGENTS.md-compatible platform

Most modern AI coding assistants support `AGENTS.md`. If yours does:
1. Open this repo
2. It should auto-load
3. If not, check your tool's docs for the equivalent of "project instructions" or "workspace rules"

---

## Platform Compatibility Matrix

| Platform | Auto-load file | File-driven context | Multi-file knowledge | Tool use |
|----------|:---:|:---:|:---:|:---:|
| **Claude Code** | `CLAUDE.md` | ✅ | ✅ Read on demand | ✅ Bash, Read, Glob |
| **Claude Codex** | `AGENTS.md` | ✅ | ✅ Read on demand | ✅ Full |
| **Cursor** | `.cursor/rules/` | ✅ | ✅ Indexed | ✅ Agent tools |
| **GitHub Copilot** | `.github/copilot-instructions.md` | ✅ | ✅ `@workspace` | Limited |
| **Windsurf** | `AGENTS.md` | ✅ | ✅ Cascade | ✅ Cascade tools |
| **ChatGPT Custom GPT** | Manual upload | ❌ | Upload up to 20 files | ❌ |
| **Claude Project** | Manual upload | ❌ | Upload files as "knowledge" | ❌ |
| **Aider** | `CONVENTIONS.md` | ✅ | ❌ Git-tracked only | ✅ CLI |
| **Continue.dev** | `rules/` config | ✅ | ✅ Configurable | ✅ Configurable |

---

## File Structure Reference

```
PQC_Agent/
├── AGENTS.md                           ← Universal agent definition
├── CLAUDE.md                           ← Claude Code (extended)
├── PLATFORMS.md                        ← This file
├── .cursor/rules/pqc-tutor.mdc        ← Cursor rules
├── .github/copilot-instructions.md     ← GitHub Copilot
├── database/                           ← Knowledge base (platform-agnostic)
│   ├── metadata/                       ← Parameter tables, status, benchmarks
│   ├── guides/                         ← Selection guide, comparison tables
│   ├── alg_cards/                      ← 20+ algorithm teaching cards
│   ├── lessons/                        ← Starter lessons
│   ├── mapping/                        ← Traditional-to-PQC mapping
│   └── implementation/                 ← Hardware module concepts
├── official/                            ← 35 PDF primary sources
│   ├── 01_nist_standards/
│   ├── 02_nist_reports_migration/
│   ├── 03_selected_future_standards/
│   ├── 04_nist_additional_signatures_round3/
│   ├── 05_china_related/
│   └── 06_general_surveys/
└── README.md                           ← Project overview
```

## Platform-Specific Limitations

### Context-Limited Platforms (ChatGPT, basic chat UIs)
- **Cannot** read database files on demand
- **Solution:** Pre-upload the most important files as knowledge/docs
- **Recommended uploads:** AGENTS.md + 5 key parameter/guide files

### No-Tool-Use Platforms
- **Cannot** search or grep the database
- **Solution:** The knowledge must be embedded in the context or uploaded files
- Use the **Compact Prompt** variant

### Git-Only Platforms (Aider, some CLI tools)
- **Cannot** read `official/` PDFs
- **Solution:** These platforms focus on code, not PDF reading
- The database markdown files are sufficient for most questions

---

## Testing Your Setup

Ask these questions to verify the agent is working correctly:

1. *"What is ML-KEM?"* → Should explain as a KEM, not PKE, with FIPS 203 status
2. *"What's the public key size of ML-KEM-768?"* → Should say 1184 bytes, citing parameter_tables.md
3. *"Is Falcon a final NIST standard?"* → Should say "future standard" or "FN-DSA track", NOT "yes"
4. *"Which algorithm should I use for signatures?"* → Should ask clarifying questions before recommending
5. *"What are the hardware costs of Aigis-enc?"* → Should say data not available, not fabricate

If the agent passes all 5 tests, your platform setup is correct.
