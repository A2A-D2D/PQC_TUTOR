# PQC Database Metadata v1

Generated from uploaded PDF corpus (originally `offical.zip`, now `official/`).

This package is the first metadata layer for a PQC quickstart teaching agent. It does not duplicate the PDFs. It indexes the PDFs and creates guardrails so the agent can teach concepts without inventing numbers.

## Main files

- `database/metadata/source_index.md` - all PDFs with trust tier, intended use, forbidden use, SHA-256, page count, and source URL when available.
- `database/metadata/standard_status.md` - status summary based only on the uploaded corpus.
- `database/metadata/parameter_tables.md` - curated parameter/size tables for ML-KEM, ML-DSA, and SLH-DSA, plus TODO sections for Falcon/HQC/domestic algorithms.
- `database/metadata/benchmark_tables.md` - hardware benchmark table template and comparison rules.
- `database/metadata/anti_hallucination_rules.md` - rules for preventing fabricated parameters and benchmarks.
- `database/metadata/facts_requiring_citation.md` - checklist for facts that must be cited.
- `database/alg_cards/` - first algorithm cards.
- `database/lessons/` - starter lesson files.
- `database/mapping/` - traditional-crypto-to-PQC mapping.
- `database/implementation/` - conceptual hardware module notes.

## Corpus summary

- PDF files indexed: 35
- Generated date: 2026-06-23

## Recommended integration

Place this folder next to your PDF folder, or copy `database/metadata/` into `pqc-quickstart-tutor/database/metadata/`.

Expected layout:

```text
pqc-quickstart-tutor/
├── database/
│   ├── official/              # your PDF corpus (local-only)
│   ├── metadata/              # files from this package
│   ├── alg_cards/
│   ├── lessons/
│   ├── mapping/
│   └── implementation/
└── skill.md
```

## Most important rule

Concepts may be explained, but numerical claims must be sourced.
