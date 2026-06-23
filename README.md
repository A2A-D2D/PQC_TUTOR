# PQC Quickstart Tutor — 后量子密码快速入门讲师

A teaching-oriented post-quantum cryptography agent for engineers and researchers. **Download. Open. Ask.** No API keys, no servers, no dependencies.

## 🚀 Quick Start (5 seconds)

```bash
# Step 1: Open in your AI tool
cd PQC_Agent
claude            # or: codex ., cursor ., windsurf ., code .

# Step 2: Just ask — the agent auto-activates
"Explain ML-KEM like you would ECDH"
"Compare Falcon vs ML-DSA key sizes"
"Which PQC signature should I use for IoT?"
```

That's it. The agent loads `CLAUDE.md` automatically. All answers are sourced from the verified database.

### Or use the one-click launcher

```bash
.\install.bat          # One-time setup (adds to PATH, creates shortcuts)
pqc-tutor              # Launch from anywhere
pqc-tutor "query"      # One-shot question from anywhere
```

### In other AI tools, same experience:

| You type... | In this tool... | What happens |
|---|---|---|
| `@PQC_AGENT explain Falcon` | Cursor | Opens agent context from `.cursor/rules/` |
| `/pqc` | Claude Code | Activates PQC Tutor slash command |
| `@workspace what is ML-KEM` | GitHub Copilot | Uses `.github/copilot-instructions.md` |
| Just ask a PQC question | Any tool in this folder | Agent auto-detects and activates |

Full setup guide: **[PLATFORMS.md](PLATFORMS.md)**

## 📊 What's Inside

### Knowledge Base (52 Markdown files)
- **Parameter tables:** Every PQC algorithm's exact key/signature/ciphertext sizes (verified against source PDFs)
- **Algorithm cards:** 20+ one-page teaching cards (ML-KEM → SQIsign)
- **Guides:** Algorithm selection decision tree + panoramic cross-algorithm comparison
- **Benchmarks:** Hardware (Falcon FPGA + ASIC) + Software (HQC, Aigis, Scloud+)
- **Standard status:** Precise NIST/China standardization tracking
- **Anti-hallucination rules:** Guardrails to prevent fabricated numbers

### Primary Sources (35 PDFs)
- FIPS 203/204/205 (NIST PQC standards)
- Falcon, HQC specifications (selected future standards)
- 9 NIST Additional Signature Round 3 candidate specs
- 8 China-related papers/drafts (Aigis, CTRU, NEV, Scloud+, LAC)
- NIST migration reports, surveys

### Algorithm Coverage (25+ algorithms)

| Category | Algorithms |
|----------|-----------|
| ✅ FIPS Standards | ML-KEM, ML-DSA, SLH-DSA |
| 🔶 Future Standards | Falcon/FN-DSA, HQC |
| 🔷 Round 3 Candidates | FAEST, HAWK, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign, UOV |
| 🔬 China Research | Aigis-enc, Aigis-sig, Scloud+, CTRU/CNTR, NEV, LAC |

## 🎯 Who This Is For

- **Software engineers** integrating PQC into TLS/SSH/VPN
- **Hardware/FPGA engineers** evaluating PQC implementation cost
- **Security architects** planning PQC migration
- **Researchers** needing quick parameter lookups
- **Students** learning PQC from a conventional-crypto background

## 🛡️ Anti-Hallucination

The agent is built on a strict rule: **concepts may be explained freely, but numerical claims must be sourced from the database.** It will say "not available" rather than fabricate parameters, sizes, or benchmarks.

## 📁 Project Structure

```
PQC_Agent/
├── AGENTS.md                           ← Universal agent definition
├── CLAUDE.md                           ← Claude Code (extended)
├── PLATFORMS.md                        ← Multi-platform setup guide
├── README.md                           ← This file
├── .cursor/rules/pqc-tutor.mdc        ← Cursor rules
├── .github/copilot-instructions.md     ← GitHub Copilot
├── database/
│   ├── metadata/                       ← Parameter tables, status, benchmarks
│   ├── guides/                         ← Selection guide, comparison tables
│   ├── alg_cards/                      ← 20+ algorithm teaching cards
│   ├── lessons/                        ← Starter lessons
│   ├── mapping/                        ← Traditional-to-PQC mapping
│   └── implementation/                 ← Hardware module concepts
└── offical/                            ← 35 PDF primary sources
    ├── 01_nist_standards/              ← FIPS 203, 204, 205
    ├── 02_nist_reports_migration/
    ├── 03_selected_future_standards/    ← Falcon, HQC specs
    ├── 04_nist_additional_signatures_round3/
    ├── 05_china_related/               ← Aigis, CTRU, NEV, Scloud+, LAC
    └── 06_general_surveys/
```

## 🔧 Using as a Library

The `database/` files are plain Markdown. You can:

- **Read them directly** — all tables in standard Markdown format
- **Use with any LLM** — copy the compact prompt from `AGENTS.md`
- **Integrate into docs** — embed algorithm cards in your own documentation
- **Extend with new PDFs** — add to `offical/`, update `source_index.md`, extract parameters

## 📝 Database Versions

| Version | What changed |
|---------|-------------|
| v1 | Initial metadata layer: ML-KEM, ML-DSA, SLH-DSA parameter tables, anti-hallucination rules |
| v2 | Added Falcon, HQC, Aigis, Scloud+, CTRU, NEV extended parameters + software benchmarks |
| v3 | Added 9 NIST Additional Signatures Round 3 candidate tables + algorithm cards |

## ✅ Verification Status

All parameter tables verified against source PDFs: **2026-06-23**

- ML-KEM, ML-DSA, SLH-DSA ✅
- Falcon, HQC ✅
- Aigis-enc, Aigis-sig ✅
- Scloud+ ✅
- CTRU/CNTR (paper) ✅
- CTRU Chinese draft ✅
- NEV ✅
- FAEST, HAWK, UOV, SQIsign, MAYO, SNOVA, SDitH, MQOM, QR-UOV ✅
