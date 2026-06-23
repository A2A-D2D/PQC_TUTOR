# Demo: Choosing a PQC Signature Algorithm

> A real agent response showing the agent's constraint-based selection reasoning.

---

**User:** "Which PQC signature should I use for IoT firmware signing?"

**Agent response:**

Good question. Let me break this down before recommending.

---

## Clarifying Questions (asked before recommending)

"Before I give you a recommendation, I need to clarify a few things about your use case:"

| Question | Why it matters |
|---|---|
| **Must it be a FIPS standard today?** | ML-DSA (FIPS 204) and SLH-DSA (FIPS 205) are final. Falcon is on the selected/in-development FIPS track (not yet final). |
| **How much bandwidth can you tolerate?** | IoT devices often have tight flash/transport constraints. sig sizes range from 96 B to 49 KB. |
| **Verification speed or signing speed?** | Many IoT devices verify far more often than they sign (firmware update = verify once, sign rarely). |
| **What's your risk tolerance?** | Conservative (want non-lattice backup)? Hash-based SLH-DSA. OK with lattice? ML-DSA or Falcon. |
| **Is implementation complexity a concern?** | Falcon requires Gaussian sampling over FFT — famously hard to implement correctly. |

---

## Assuming: IoT Firmware Signing

Let's reason through this: firmware signing typically means:
- **Sign rarely** (dev build server) → signing speed is not critical
- **Verify on-device** (potentially constrained CPU) → verification speed matters
- **Signatures travel in firmware packages** → signature size matters for OTA bandwidth
- **Standard compliance** → FIPS standard strongly preferred for commercial products

---

## Head-to-Head: ML-DSA vs Falcon vs SLH-DSA

*All numbers from database/metadata/parameter_tables.md and extended tables.*

| Dimension | ML-DSA-44 (FIPS 204) | Falcon-512 (future FN-DSA) | SLH-DSA-128s (FIPS 205) |
|---|---|---|---|
| **Standard status** | ✅ FIPS 204 | 🔶 Selected, not final | ✅ FIPS 205 |
| **Security category** | NIST Level 2 | NIST Level 1 | NIST Level 1 |
| **Public key** | 1312 B | 897 B | **32 B** |
| **Signature** | 2420 B | **666 B** | 7856 B |
| **pk + sig (total)** | 3732 B | **1563 B** | 7888 B |
| **Verification speed** | ⭐⭐⭐ Fast | ⭐⭐ Moderate | ⭐ Slow (hash-heavy) |
| **Implementation** | ⭐⭐ Moderate | ⭐⭐⭐⭐ Hard (Gaussian) | ⭐⭐ Moderate (hash trees) |
| **Security assumption** | Lattice (MLWE) | Lattice (NTRU) | **Hash-based (no lattice)** |

---

## My Recommendation

### 🥇 Primary: ML-DSA-44 (FIPS 204)

**Why:**
- Final FIPS standard — no regulatory risk
- Easiest lattice signature to implement correctly (no Gaussian sampling needed)
- Fast verification on embedded devices
- Total 3732 B per firmware update is manageable for most IoT

**Trade-off:** 2420 B signature. If bandwidth is very tight, this may be painful.

### 🥈 For bandwidth-constrained: Falcon-512

**Why:**
- Only 666 B signature — **3.6x smaller than ML-DSA-44**
- Total pk+sig is just 1563 B (less than half of ML-DSA)
- On the FN-DSA/FIPS 206 selected standardization track (not yet final)

**Trade-off:** Not yet a FIPS standard. Gaussian sampling is implementation-hard (many side-channel pitfalls). Only NIST Level 1 security.

### 🥉 For maximum conservatism: SLH-DSA-128s

**Why:**
- Not lattice-based — hash-based (WOTS+ / Merkle trees)
- Final FIPS 205 standard
- Only 32 B public key
- Immune to lattice cryptanalysis advances

**Trade-off:** 7856 B signature — big for IoT firmware updates. Slow verification (many hash calls).

---

## Side-by-Side Bandwidth Comparison (visual)

```
Signature bytes per algorithm (NIST Level 1-2):

ML-DSA-44   ████████████▌ 2420 B
Falcon-512  ███▎ 666 B
SLH-DSA     ███████████████████████████████████████ 7856 B
UOV uov-Is  ▌ 96 B (⚠ pk=66KB, Round 3 candidate)
SQIsign     ▊ 148 B (⚠ extremely complex, Round 3 candidate)
```

---

## Decision Summary

```
IoT Firmware Signing
├── FIPS standard required?
│   ├── YES, bandwidth OK → ML-DSA-44 ✅
│   ├── YES, most conservative → SLH-DSA-128s ✅
│   └── NO (can wait for FIPS 206) → Falcon-512 🥇 (bandwidth winner)
└── Non-standard OK (research/PoC)?
    ├── HAWK-512 (sig=555B, pk=1024B) — NTRU-based, Round 3
    └── SQIsign (sig=148B, pk=65B) — extremely complex, experimental
```

---

## One More Thing

If you can use **hybrid mode** (ECDSA + ML-DSA, both must verify), this gives you:
- ECDSA for existing IoT fleet compatibility
- ML-DSA for quantum resistance
- Zero trust in either algorithm alone (defense-in-depth)

This is the approach NIST SP 800-227 recommends for PQC migration.

---

*This demo shows the agent's constraint-based selection approach: ask clarifying questions, consult the selection guide, rank recommendations with exact parameter data, show visual comparisons, and explain trade-offs. All numbers from database/guides/algorithm_selection_guide.md and database/metadata/parameter_tables.md.*
