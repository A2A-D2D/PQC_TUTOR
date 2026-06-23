# Database Quick Index

Quick reference for which file to read for which question. Full inventory at `database/index.json`.

## Algorithm Parameters

| Question | File |
|----------|------|
| ML-KEM key sizes (FIPS 203) | `database/metadata/parameter_tables.md` |
| ML-DSA key/sig sizes (FIPS 204) | `database/metadata/parameter_tables.md` |
| SLH-DSA sizes (FIPS 205) | `database/metadata/parameter_tables.md` |
| Falcon, HQC, Aigis, Scloud+, CTRU, NEV | `database/metadata/parameter_tables_extended.md` |
| Round 3 candidates (9 algorithms) | `database/metadata/additional_signatures_round3_tables.md` |

## Status & Standards

| Question | File |
|----------|------|
| Is X a NIST standard? | `database/metadata/standard_status.md` |
| What PDFs do we have? | `database/metadata/source_index.md` |
| Which PDF pages have tables? | `database/extraction_notes/source_pages.md` |

## Recommendations & Comparisons

| Question | File |
|----------|------|
| Which algorithm should I pick? | `database/guides/algorithm_selection_guide.md` |
| Compare all KEMs/Sigs side-by-side | `database/guides/cross_algorithm_comparison.md` |
| Traditional → PQC concept mapping | `database/mapping/traditional_crypto_to_pqc.md` |

## Benchmarks

| Question | File |
|----------|------|
| Hardware (FPGA/ASIC) data | `database/metadata/benchmark_tables.md` |
| Software/CPU performance | `database/metadata/software_benchmark_tables.md` |

## Teaching & Rules

| Question | File |
|----------|------|
| Anti-hallucination guardrails | `database/metadata/anti_hallucination_rules.md` |
| Algorithm teaching cards | `database/alg_cards/<algo>_card.md` |
| Starter lessons | `database/lessons/` |
| Hardware module concepts | `database/implementation/pqc_hardware_modules.md` |

## Database Stats

- 38 Markdown files across 7 categories
- 25+ algorithms covered
- 35 source PDFs (local-only, not committed)
- Parameter tables verified against source PDFs
