# Local PDF Corpus — 本地 PDF 文献库

This directory holds the primary-source PDFs used to verify all parameter tables and algorithm cards in `database/`.

**These PDFs are NOT committed to GitHub.**
- `official/` is listed in `.gitignore`
- `*.pdf` is listed in `.gitignore`

## Why local-only?

- PDFs are large (35 files, hundreds of MB)
- Copyright varies by source (NIST public domain, academic papers with author copyright, China-related research papers)
- The extracted knowledge (parameter tables, algorithm cards, guides) is in `database/` — that IS committed

## Expected corpus

See `database/metadata/source_index.md` for the complete list of expected PDFs and their trust tiers.

```
official/
├── 01_nist_standards/                  ← FIPS 203, 204, 205 + SP 800-227
├── 02_nist_reports_migration/          ← NIST IR 8105, 8413, 8528, 8545, 8547, 8610
├── 03_selected_future_standards/       ← Falcon spec, FN-DSA status, HQC spec
├── 04_nist_additional_signatures_round3/ ← 9 candidate specs
├── 05_china_related/                   ← Aigis, CTRU, NEV, Scloud+, LAC
├── 06_general_surveys/                 ← Surveys, migration guides
└── 00_manifest/                        ← File list and collection notes
```

## How to obtain the PDFs

The source PDFs are mostly available for free download:
- NIST publications: https://csrc.nist.gov/pubs
- Round 3 candidate specs: linked from NIST's PQC page
- China-related papers: from respective academic/institutional websites

## How to add new PDFs

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the 7-step workflow.
