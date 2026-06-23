# v0.1.0 — First Public Release

**Released: 2026-06-23**

The first public release of **PQC Quickstart Tutor** (后量子密码快速入门讲师), a teaching-oriented post-quantum cryptography knowledge base for engineers and researchers.

---

## ✅ What's Included

### Knowledge Base (38 verified Markdown files)
- **9 metadata files:** Parameter tables (ML-KEM, ML-DSA, SLH-DSA, Falcon, HQC, Aigis, Scloud+, CTRU, NEV), Round 3 candidate tables, hardware/software benchmarks, anti-hallucination rules
- **22 algorithm cards:** One-page teaching cards covering all 25+ algorithms
- **2 strategy guides:** Algorithm selection decision tree + panoramic cross-algorithm comparison
- **2 starter lessons:** Why PQC, PQC algorithm map
- **2 implementation docs:** Traditional-to-PQC mapping, hardware module concepts
- **1 extraction note:** Source PDF page references

### Primary Sources (35 PDFs, local only)
- FIPS 203/204/205 (NIST PQC standards)
- Falcon, HQC specs (selected for standardization, FIPS not yet final)
- 9 NIST Additional Signature Round 3 candidate specs
- 9 China-related papers/drafts
- NIST migration reports and surveys

### Platform Support (7 platforms)
- Claude Code (CLAUDE.md + /pqc slash command)
- Claude Codex (AGENTS.md)
- Cursor (.cursor/rules/pqc-tutor.mdc)
- GitHub Copilot (.github/copilot-instructions.md)
- Windsurf (AGENTS.md)
- Custom GPT / Claude Project (compact prompt)
- Any AGENTS.md-compatible platform

### Tooling & CI
- `tools/check_database.py` — 7 integrity checks (passing)
- `.github/workflows/check.yml` — auto-check on push/PR
- `database/index.json` — machine-readable file inventory
- `install.bat` / `pqc-tutor.bat` — Windows launcher scripts

### Documentation
- Bilingual README (EN + 中文)
- Live demos: ML-KEM explanation, signature selection
- Multi-platform setup guide (PLATFORMS.md)
- Contribution guide (CONTRIBUTING.md)
- Apache 2.0 LICENSE + NOTICE.md

---

## 🔧 Changes Since Initial Commit

- Fixed: Absolute paths → relative paths throughout
- Fixed: `offical/` directory renamed to `official/`
- Fixed: Removed `.claude/settings.local.json` (local-only)
- Added: LICENSE (Apache 2.0) and NOTICE.md
- Added: Database index and integrity checker
- Added: GitHub Actions CI workflow
- Added: Live demo documents
- Added: Bilingual README (EN + 中文)
- Added: Contribution guide

---

## 🤝 How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). We welcome:
- New algorithm parameter tables
- Algorithm teaching cards
- Hardware/software benchmarks
- Chinese/English translations
- Platform integrations

---

## 📄 License

Apache License 2.0. See [LICENSE](LICENSE).
