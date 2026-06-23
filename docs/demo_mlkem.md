# Demo: Explaining ML-KEM to an ECDH User

> A real agent response showing the PQC Quickstart Tutor teaching pattern.

---

**User:** "Explain ML-KEM to someone who understands ECDH."

**Agent response:**

## ML-KEM ≈ ECDH in protocol role (analogy)

*This is an analogy, not a mechanical equivalence.*

Think of ML-KEM the way you think of ECDH: both are used to **establish a shared secret** between two parties over an insecure channel. In TLS 1.3, ECDH is what makes the handshake work — Alice sends her ephemeral public key, Bob replies with his, and they both derive the premaster secret. ML-KEM fills the same slot in a PQC migration.

But the mechanics are completely different.

---

## One-Sentence Conclusion

**ML-KEM (FIPS 203) is a lattice-based Key Encapsulation Mechanism where Bob encapsulates a shared secret under Alice's public key, and Alice decapsulates it — the lattice problem (Module-LWE) makes it hard for an attacker to recover the secret from the public key and ciphertext.**

---

## What ML-KEM IS and IS NOT

| ✅ ML-KEM is... | ❌ ML-KEM is NOT... |
|---|---|
| A KEM (KeyGen / Encaps / Decaps) | A PKE (does not encrypt arbitrary messages) |
| Like ECDH in *protocol role* | Like ECDH in math (it's not a curve) |
| Based on Module-LWE (lattices) | Based on RSA/ECC math |
| FIPS 203 (NIST standard) | A general-purpose encryption scheme |

---

## The Three Functions

```
KeyGen() → (pk, sk)
  Alice generates her keypair. pk is ~1184 bytes (ML-KEM-768).

Encaps(pk) → (ct, ss)
  Bob uses Alice's pk to produce a ciphertext ct (~1088 bytes)
  and a shared secret ss (32 bytes). He sends ct to Alice.

Decaps(sk, ct) → ss
  Alice uses her secret key to recover the same shared secret ss.
```

The critical guarantee: if ct is honestly generated under pk, Decaps(sk, ct) = ss.

---

## Core Math Idea (intuition only)

Module-LWE says: given a matrix **A** and a noisy product **t = A·s + e**, finding **s** is hard (even for quantum computers). ML-KEM builds KEM from this.

**NTT replaces scalar multiplication.** In ECDH, you do `d·G`. In ML-KEM, the dominant operation is NTT (Number Theoretic Transform) — essentially FFT over a polynomial ring. This turns O(n²) polynomial multiplication into O(n log n).

---

## Implementation / Dataflow View

```
              │Alice's machine       │Bob's machine       │
              │                      │                    │
 KeyGen:      │Sample s (secret)     │                    │
              │A ← matrix from seed  │                    │
              │t = A·s + e (noise)   │                    │
              │pk = (seed_A, t)      │                    │
              │                      │                    │
 Encaps:      │                      │pk received ←──────│
              │                      │Sample m           │
              │                      │ct = encrypt(m, pk)│
              │                      │ss = KDF(m, ...)   │
              │                      │ct sent ──────────→│
              │                      │                    │
 Decaps:      │m ← decrypt(ct, sk)   │                    │
              │ss = KDF(m, ...)      │                    │
              │                      │                    │
              │     Both now have ss │                    │
```

---

## ML-KEM Parameter Sets

*From FIPS 203; verified against NIST_FIPS_203_ML-KEM_2024.pdf, Table 2-3.*

| Parameter set | Security category | pk (B) | sk (B) | ct (B) | ss (B) |
|---|---|---|---|---|---|
| ML-KEM-512 | 1 (≈AES-128) | 800 | 1632 | 768 | 32 |
| **ML-KEM-768** | **3 (≈AES-192)** | **1184** | **2400** | **1088** | **32** |
| ML-KEM-1024 | 5 (≈AES-256) | 1568 | 3168 | 1568 | 32 |

> **Recommendation:** ML-KEM-768 is the safest default — Category 3 security, balanced sizes.

---

## Common Misunderstandings

1. **"ML-KEM encrypts messages"** → No. A KEM establishes a shared secret. Use DEM (Data Encapsulation Mechanism, e.g., AES-GCM) for encryption.
2. **"ML-KEM replaces RSA encryption"** → No. It replaces the key-establishment part of RSA-KEM or ECDH. Symmetric encryption (AES) remains.
3. **"ML-KEM-512 is AES-128"** → NIST Category 1 is *comparable* to, but not literally, 128-bit security.
4. **"NTT is a crypto primitive"** → No. NTT is an algorithm (≈FFT). The security comes from Module-LWE.

---

*This demo shows the "Known → New" teaching pattern: start with ECDH analogy, give the conclusion, explain the flow, show implementation view, correct misunderstandings. All numbers sourced from database/parameter_tables.md.*
