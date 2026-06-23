# Contributing to PQC Quickstart Tutor

Thanks for helping improve this teaching agent! Here's how to contribute new knowledge to the database.

## Quick Contribution Checklist

- [ ] I have read `database/metadata/anti_hallucination_rules.md`
- [ ] All numeric claims are verified against primary source PDFs
- [ ] I have updated `database/metadata/source_index.md` (if adding PDFs)
- [ ] I ran `python tools/check_database.py` and it passes
- [ ] Algorithm status labels are correct (✅/🔶/🔷)
- [ ] No absolute paths, no local machine references

---

## How to Add a New PDF Source

### Step 1: Place the PDF

Put the PDF in the correct subdirectory under `official/`:

```
official/
├── 01_nist_standards/           ← FIPS, NIST SP documents
├── 02_nist_reports_migration/   ← NIST IR series
├── 03_selected_future_standards/ ← Falcon, HQC specs
├── 04_nist_additional_signatures_round3/  ← Round 3 candidates
├── 05_china_related/            ← China-related papers/drafts
└── 06_general_surveys/          ← Surveys, general PQC papers
```

⚠️ PDFs are in `.gitignore` and will NOT be committed. They are local-only.

### Step 2: Register the PDF in source_index.md

Add an entry to `database/metadata/source_index.md`:

```markdown
| File | Trust Tier | Category | Can use for... | Must NOT use for... |
|------|-----------|----------|----------------|---------------------|
| official/04_nist_additional_signatures_round3/NEW_ALGO_v2_spec.pdf | Tier 1 | Candidate Spec | Parameter lookup, algorithm description | Standardization claims |
```

### Step 3: Extract Parameters

Extract key/signature/ciphertext sizes from the PDF and add to the right table:

- **FIPS standards** → `database/metadata/parameter_tables.md`
- **Extended algorithms** → `database/metadata/parameter_tables_extended.md`
- **Round 3 candidates** → `database/metadata/additional_signatures_round3_tables.md`

Rules for extraction:
- Copy EXACTLY what's in the PDF table. Never round, never infer.
- If a field is unclear, mark it `TODO` — don't guess.
- Always cite the PDF page/table number.
- Mark unverified rows explicitly.

### Step 4: Update Standard Status

If the algorithm has NIST/China status changes, update `database/metadata/standard_status.md`.

### Step 5: Create an Algorithm Card

Create `database/alg_cards/<algo_name>_card.md` using this template:

```markdown
# <ALGORITHM NAME> — One-Page Card

## Identity
- **Full name:** ...
- **Type:** KEM / Signature
- **Family:** Lattice (Module-LWE) / Code-based / Hash-based / Multivariate / Isogeny
- **Status:** ✅ FIPS Standard / 🔶 Selected (FIPS track) / 🔷 Round 3 Candidate / 🔬 Research
- **Standard doc:** FIPS XXX / specification version X.X

## Traditional Analogy
- Closest conventional equivalent: ECDH / ECDSA / etc.
- **Analogy, not equivalence.**

## One-Sentence Summary
...

## Main Operations
1. KeyGen() → (pk, sk)
2. Encaps(pk) → (ct, ss) / Sign(sk, msg) → sig
3. Decaps(sk, ct) → ss / Verify(pk, msg, sig) → T/F

## Parameter Table
| Parameter set | Security | pk (B) | sk/ct (B) | Source |
|---|---|---|---|---|
| ... | ... | ... | ... | PDF p.X |

## Core Math (intuition)
...

## Implementation Notes
- Dominant computation: ...
- Key modules: ...
- Known challenges: ...

## Common Misunderstandings
- "X does Y" → No. ...

## Source
- `official/.../<filename>.pdf`, Table X / Section Y
```

### Step 6: Update index.json

Add the new files to `database/index.json` under the appropriate category.

### Step 7: Run the Checker

```bash
python tools/check_database.py
```

Fix any errors before submitting.

---

## How to Add a Benchmark Entry

1. Add to `database/metadata/benchmark_tables.md` (hardware) or `software_benchmark_tables.md` (software)
2. **Always include:** algorithm + parameter set, implementation type, platform/device/process, frequency, cycles/time, memory included?, masking/side-channel protection?, source table/section
3. **Never** compare across different platforms/papers without stating the caveat

---

## How to Update the Algorithm Selection Guide

Edit `database/guides/algorithm_selection_guide.md`. The guide is organized as:

1. Quick selection (safe defaults)
2. Decision flow (Step 1 → 2A/2B)
3. Constraint-based matrix (bandwidth, speed, simplicity, conservatism)
4. Cross-algorithm comparison

When adding a new algorithm recommendation:
- Always show standard status (✅/🔶/🔷)
- Include exact key/sig/ct sizes from parameter tables
- State implementation difficulty qualitatively
- Highlight trade-offs

---

## Style Guide

### File Naming
- Markdown files: `lowercase_with_underscores.md`
- Algorithm cards: `<algo_name>_card.md` (e.g., `falcon_card.md`)
- No spaces in filenames

### Status Labels (exact — do not vary)
- ✅ **FIPS Standard:** FIPS 203/204/205 final standard
- 🔶 **Selected/In-Development:** selected for standardization track, no final FIPS in corpus
- 🔷 **Round 3 Candidate:** NIST Additional Signature Round 3 candidate only
- 🔬 **Research/Domestic:** research material or domestic candidate, NOT NIST standard

### Anti-Hallucination Rules (from database/metadata/anti_hallucination_rules.md)
1. Concepts may be explained freely
2. Numeric claims MUST be sourced
3. Never fabricate: parameters, key sizes, security categories, NIST status, FPGA/ASIC numbers, benchmarks, "best"/"fastest" claims
4. If data unavailable: say "not available in the current database"
5. Always cite the source file/table

---

## Testing

Before submitting a PR:

```bash
# 1. Run the database checker
python tools/check_database.py

# 2. Check for absolute paths
python tools/check_database.py --json | python -c "import sys,json; d=json.load(sys.stdin); print(d['checks']['absolute_paths'])"

# 3. Verify the index is up to date
find database -name '*.md' | wc -l  # should match index.json total_markdown_files
```

---

## Questions?

Open an issue. If you're adding a new algorithm, start a discussion first — we'll help you categorize it correctly.

Together we make PQC more accessible to engineers everywhere. 🚀
