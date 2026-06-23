# PQC Anti-Hallucination Evals

Golden tests that validate the agent profile's ability to prevent hallucination.

## Files

- `golden_tests.md` — 40 human-readable Q&A pairs across 7 categories
- `golden_tests.json` — Machine-readable version for automated runners

## Categories

| # | Category | Tests | Validates |
|---|----------|:-----:|-----------|
| A | Standard Status | 10 | Never call a candidate a "standard" |
| B | Parameter Lookups | 10 | Exact numbers from database only |
| C | KEM/PKE/Sig Confusion | 5 | Never conflate KEM with encryption or signature |
| D | Benchmark Hallucination | 5 | Never invent hardware numbers |
| E | "Not Available" Boundary | 5 | Admit knowledge gaps explicitly |
| F | Algorithm Family | 5 | Correct lattice/hash/code/isogeny/multivariate families |
| G | Source Citation | 5 | Every number has a traceable source |

**Total: 40 tests**

## How to Run

These tests are designed for human-in-the-loop evaluation:

1. Load this skill in Claude Code, Codex, Cursor, or any LLM runtime
2. Ask each question from `golden_tests.md`
3. Check the response against "Must NOT say" constraints
4. Score: pass/fail

Target: 100% on categories A–D and G; ≥80% on category E.

## Automated Runner (future)

A script that calls the Claude API with this skill loaded and scores
each Q&A pair against the expected constraints is planned for v0.2.0.

## Adding New Tests

1. Identify a hallucination risk (e.g., new algorithm, new benchmark source)
2. Write the Q&A pair with "Must NOT say" constraints
3. Add to the appropriate category in `golden_tests.md`
4. Update `golden_tests.json`

Every test must reference a specific database file or rule.
