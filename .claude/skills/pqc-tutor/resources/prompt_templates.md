# Prompt Templates — PQC Teaching Patterns

Reusable answer structures. Adapt to the specific question; always cite database files for numerical claims.

## 1. Explaining a PQC Algorithm (e.g., ML-KEM)

```
**Analogy:** ML-KEM ≈ ECDH in protocol role (shared secret establishment).
_This is an analogy, not a mechanical equivalence._

**One-sentence conclusion:** ML-KEM (FIPS 203) is a lattice-based KEM where...

**What it IS / IS NOT:**
| ✅ Is... | ❌ Is NOT... |
|----------|-------------|
| A KEM (KeyGen/Encaps/Decaps) | A PKE (doesn't encrypt messages) |
| Like ECDH in protocol role | Like ECDH in math |

**The three functions:**
1. KeyGen() → (pk, sk) — Alice generates
2. Encaps(pk) → (ct, ss) — Bob encapsulates
3. Decaps(sk, ct) → ss — Alice decapsulates

**Core math idea (intuition only):** Module-LWE...

**Implementation/dataflow:** [show data movement diagram]

**Common misunderstandings:**
- "ML-KEM encrypts messages" → No. KEM → shared secret; use DEM for encryption.

**Parameter table (from database):** [cite table]
```

## 2. Choosing an Algorithm

```
**Clarifying questions first:**
1. KEM or Signature?
2. Must it be a FIPS standard today?
3. Primary constraint? (bandwidth / speed / simplicity / conservatism)
4. What's the deployment environment?

**Recommendation (ranked):**
🥇 Primary: [algo] — reason, sizes from database
🥈 Alternative: [algo] — reason, sizes from database
🥉 Conservative backup: [algo] — reason

**Side-by-side comparison table:** [from selection guide]
**Decision tree:** [from selection guide]
```

## 3. Comparing Algorithms

```
Always include status column (✅/🔶/🔷) so users understand maturity differences.

| Algorithm | Status | pk (B) | sig/ct (B) | Family | Notes |
|-----------|--------|--------|-----------|--------|-------|
| ... | ... | ... | ... | ... | ... |

**Key trade-offs:** [summarize]
**Visual comparison:** [bar chart if helpful]
```

## 4. Hardware Question

```
**Dominant computation:** [NTT / hash / sampling / ...]
**Memory/data-movement bottlenecks:** [identify]
**Reusable modules:** [Keccak, NTT, sampling, modular arithmetic, packing]
**Qualitative area/latency/throughput trade-offs:** [discuss]
**Verification concerns:** [mention]

⚠️ NEVER fabricate LUT/FF/DSP/BRAM/cycle numbers.
If data is not in benchmark_tables.md, say so explicitly.
```

## 5. Correcting a Misunderstanding

```
"That's a common misunderstanding. Here's the correction:"

❌ Wrong: "[user's claim]"
✅ Correct: "[accurate statement]"

**Why this matters:** [practical implication]
**How to keep it straight:** [mnemonic or simple rule]
```
