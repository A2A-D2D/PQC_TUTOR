# PQC Algorithm Panoramic Comparison — 后量子密码算法全景对比

This file provides a cross-algorithm comparison of all PQC algorithms in the database. All values are sourced from the parameter tables in `database/metadata/`. For full details on any algorithm, follow the source reference.

**Last verified:** 2026-06-23

---

## KEM Algorithm Comparison

### Primary KEMs (Standards + Future Standards)

| Algorithm | Status | Security | pk (B) | sk (B) | ct (B) | ss (B) | Bandwidth (pk+ct) | DFR | Family |
|---|---|---|---|---|---|---|---|---|---|
| **ML-KEM-512** | ✅ FIPS 203 | NIST-1 (128b) | 800 | 1632 | 768 | 32 | 1568 | <2⁻¹³⁹ | Module-LWE |
| **ML-KEM-768** | ✅ FIPS 203 | NIST-3 (192b) | 1184 | 2400 | 1088 | 32 | 2272 | <2⁻¹⁶⁴ | Module-LWE |
| **ML-KEM-1024** | ✅ FIPS 203 | NIST-5 (256b) | 1568 | 3168 | 1568 | 32 | 3136 | <2⁻¹⁷⁴ | Module-LWE |
| **HQC-1** | 🔶 Future Std | NIST-1 | 2241 | 2321 | 4433 | 32 | 6674 | <2⁻¹²⁸ | Code (QC-MDPC) |
| **HQC-3** | 🔶 Future Std | NIST-3 | 4514 | 4602 | 8978 | 32 | 13492 | <2⁻¹⁹² | Code (QC-MDPC) |
| **HQC-5** | 🔶 Future Std | NIST-5 | 7237 | 7333 | 14421 | 32 | 21658 | <2⁻²⁵⁶ | Code (QC-MDPC) |

**Key takeaway:** ML-KEM wins on bandwidth (2-6× smaller than HQC). HQC provides algorithmic diversity (code-based, not lattice).

### China-Related KEMs

| Algorithm | Status | Security (C/Q) | pk (B) | sk (B) | ct (B) | ss (B) | Bandwidth | DFR | Family |
|---|---|---|---|---|---|---|---|---|---|
| **Aigis-enc II** ★ | 🔷 研究 推荐 | 162 / 128 | 896 | 1152 (compact: 32) | 992 | 32 | 1888 | 2⁻¹²⁸ | AMLWE |
| Aigis-enc I | 🔷 研究 | 111 / 80 | 672 | 928 | 672 | 32 | 1344 | 2⁻⁸² | AMLWE |
| Aigis-enc III | 🔷 研究 | 235 / 192 | 1472 | 1984 | 1536 | 64 | 3008 | 2⁻²¹¹ | AMLWE |
| **CTRU-768 (草案)** ★ | 🔷 征求意见稿 | 192 / 173 | 1152 | 1584 | 960 | 48 | 2112 | — | NTRU+RLWE |
| CTRU-576 (草案) | 🔷 征求意见稿 | 142 / 128 | 864 | 1260 | 720 | 36 | 1584 | — | NTRU+RLWE |
| CTRU-1024 (草案) | 🔷 征求意见稿 | 255 / 231 | 1536 | 2112 | 1280 | 64 | 2816 | — | NTRU+RLWE |
| CTRU-Light | 🔷 征求意见稿 | 125 / 114 | 640 | 864 | 512 | 32 | 1152 | — | NTRU+RLWE |
| CTRU-Prime | 🔷 征求意见稿 | 173 / 157 | 1237 | 1666 | 952 | 48 | 2189 | — | NTRU (prime field) |
| **CTRU (论文) n=768** ★ | 🔷 论文 | 181 / 164 | 1152 | — | 960 | — | 2112 | 2⁻¹⁸⁴ | NTRU+RLWE |
| CNTR n=768 | 🔷 论文 | 191 / 173 | 1152 | — | 960 | — | 2112 | 2⁻²³⁰ | NTRU+RLWR |
| **NEV-512** ★ | 🔷 论文 | 141 (LWE est.) | 615 | 1294 | 615 | — | 1230 | 2⁻¹³⁸ | NTRU+RLWE |
| NEV'-512 | 🔷 论文 | 145 (LWE est.) | 615 | 1294 | 615 | — | 1230 | 2⁻²⁰⁰ | NTRU+sspRLWE |
| NEV-1024 | 🔷 论文 | 281 (LWE est.) | 1229 | 2522 | 1229 | — | 2458 | 2⁻¹⁵² | NTRU+RLWE |
| **Scloud+-128** ★ | 🔷 论文 | 136C / 123Q | 7200 | — | 5456 | 16 | 12656 | 2⁻¹³⁴ | Unstructured LWE |
| Scloud+-192 | 🔷 论文 | 200C / 184Q | 11136 | — | 10832 | 24 | 21968 | 2⁻²⁰¹ | Unstructured LWE |
| Scloud+-256 | 🔷 论文 | 263C / 242Q | 18744 | — | 16916 | 32 | 35660 | 2⁻²⁶⁶ | Unstructured LWE |

★ = recommended/default parameter set for that algorithm.

**Key takeaway:** NEV achieves the smallest bandwidth (1230B at 128-bit) among all KEMs in the database, but is a research paper, not a standard. Scloud+ has the largest keys (unstructured LWE trade-off).

---

## Signature Algorithm Comparison

### Primary Signatures (Standards + Future Standards)

| Algorithm | Status | Security | pk (B) | sk (B) | sig (B) | pk+sig (B) | Family | Impl. Difficulty |
|---|---|---|---|---|---|---|---|---|
| **ML-DSA-44** | ✅ FIPS 204 | NIST-2 | 1312 | 2560 | 2420 | 3732 | Module-LWE+SIS | ⭐⭐ |
| **ML-DSA-65** ★ | ✅ FIPS 204 | NIST-3 | 1952 | 4032 | 3309 | 5261 | Module-LWE+SIS | ⭐⭐ |
| ML-DSA-87 | ✅ FIPS 204 | NIST-5 | 2592 | 4896 | 4627 | 7219 | Module-LWE+SIS | ⭐⭐ |
| **SLH-DSA-128s** | ✅ FIPS 205 | NIST-1 | 32 | 64 | 7856 | 7888 | Hash (SPHINCS+) | ⭐⭐ |
| SLH-DSA-128f | ✅ FIPS 205 | NIST-1 | 32 | 64 | 17088 | 17120 | Hash (SPHINCS+) | ⭐⭐ |
| SLH-DSA-192s | ✅ FIPS 205 | NIST-3 | 48 | 96 | 16224 | 16272 | Hash (SPHINCS+) | ⭐⭐ |
| SLH-DSA-256s | ✅ FIPS 205 | NIST-5 | 64 | 128 | 29792 | 29856 | Hash (SPHINCS+) | ⭐⭐ |
| **Falcon-512** ★ | 🔶 Future Std | NIST-1 | 897 | 1281 | 666 | 1563 | NTRU (GPV) | ⭐⭐⭐⭐ |
| Falcon-1024 | 🔶 Future Std | NIST-5 | 1793 | 2305 | 1280 | 3073 | NTRU (GPV) | ⭐⭐⭐⭐ |

**Key takeaway:** Falcon offers the best pk+sig combination among standards-track signatures. SLH-DSA has tiny public keys (32B!) but huge signatures. ML-DSA is the easiest to implement.

### China-Related Signatures

| Algorithm | Status | Security (C/Q) | pk (B) | sk (B) | sig (B) | pk+sig | Family |
|---|---|---|---|---|---|---|---|
| **Aigis-sig II** ★ | 🔷 研究 推荐 | 141 / 128 | 1312 | 3376 | 2445 | 3757 | AMLWE+AMSIS |
| Aigis-sig II-b | 🔷 研究 | 141 / 128 | 1312 | 3376 | 2445 | 3757 | AMLWE+AMSIS |
| Aigis-sig I | 🔷 研究 | 98 / 80 | 1056 | 2448 | 1852 | 2908 | AMLWE+AMSIS |
| Aigis-sig III | 🔷 研究 | 178 / 160 | 1568 | 3888 | 3046 | 4614 | AMLWE+AMSIS |

---

## Cross-Algorithm Size Comparison (Visual Summary)

### KEM: Total Bandwidth (pk + ct) — lower is better

```
NEV-512          ▎▎ 1230  (研究)
CTRU-Light       ▎▎ 1152  (草案)
Aigis-enc I      ▎▎▎ 1344
ML-KEM-512       ▎▎▎ 1568  ✅ FIPS 203
CTRU-576 (草案)  ▎▎▎ 1584
Aigis-enc II     ▎▎▎▎ 1888
CTRU-768 (草案)  ▎▎▎▎ 2112
ML-KEM-768       ▎▎▎▎ 2272  ✅ FIPS 203
NEV-1024         ▎▎▎▎▎ 2458
CTRU-1024 (草案) ▎▎▎▎▎ 2816
Aigis-enc III    ▎▎▎▎▎▎ 3008
ML-KEM-1024      ▎▎▎▎▎▎ 3136  ✅ FIPS 203
HQC-1            ▎▎▎▎▎▎▎▎▎▎▎▎▎ 6674  🔶
Scloud+-128      ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 12656  (研究)
HQC-3            ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 13492  🔶
Scloud+-256      ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 35660
```

### Signature: Combined Size (pk + sig) — lower is better

```
SQIsign NIST-I    ▎ 213     (候选)
Falcon-512        ▎▎▎▎ 1563    🔶 未来标准
SQIsign NIST-III  ▎▎▎▎ 321     (候选)
SQIsign NIST-V    ▎▎▎▎ 421     (候选)
HAWK-512          ▎▎▎▎ 1579    (候选)
Aigis-sig I       ▎▎▎▎▎▎ 2908
Falcon-1024       ▎▎▎▎▎▎▎ 3073 🔶
ML-DSA-44         ▎▎▎▎▎▎▎▎▎ 3732 ✅ FIPS 204
Aigis-sig II      ▎▎▎▎▎▎▎▎▎ 3757
HAWK-1024         ▎▎▎▎▎▎▎▎▎▎ 3661 (候选)
Aigis-sig III     ▎▎▎▎▎▎▎▎▎▎▎▎ 4614
ML-DSA-65         ▎▎▎▎▎▎▎▎▎▎▎▎▎ 5261 ✅ FIPS 204
ML-DSA-87         ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 7219 ✅ FIPS 204
SLH-DSA-128s      ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 7888 ✅ FIPS 205
SLH-DSA-192s      ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 16272
SLH-DSA-256s      ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 29856
UOV uov-Is        ▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎▎ 66672 (sig=96 ⚡, pk=66KB 💣)
```

---

## Family-Level Comparison

| Family | KEM algorithms | Sig algorithms | Math assumption | Maturity | Key characteristic |
|---|---|---|---|---|---|
| **Module-Lattice** | ML-KEM | ML-DSA | MLWE / MSIS | ✅ FIPS 203/204 | Best all-around. NTT-heavy. |
| **NTRU-Lattice** | CTRU, NEV | Falcon, HAWK | NTRU | 🔶🔷 Mixed | Compact sigs (Falcon). Complex sampling (Falcon/HAWK). |
| **Hash-based** | — | SLH-DSA | Hash preimage | ✅ FIPS 205 | Most conservative. Large sigs. |
| **Code-based** | HQC | SDitH | Syndrome Decoding | 🔶🔷 Mixed | Algorithmic diversity from lattices. |
| **Multivariate** | — | UOV, MAYO, QR-UOV, SNOVA, MQOM | MQ problem | 🔷 Candidates | Small sigs. Large pubkeys. |
| **Symmetric** | — | FAEST | AES/OWF + ZK | 🔷 Candidate | Only relies on symmetric crypto. |
| **Isogeny** | — | SQIsign | Endomorphism Ring | 🔷 Candidate | Smallest keys+sigs. Very complex math. |
| **Unstructured LWE** | Scloud+ | — | Plain LWE | 🔷 Research | No algebraic structure. Largest keys. |

---

## Software Performance Comparison

⚠️ **Important:** The platforms, CPUs, compilers, and measurement methods differ across papers. These numbers are NOT directly comparable. Use for rough magnitude estimation only.

### KEM Software Benchmarks

| Algorithm | Platform | KeyGen | Encaps | Decaps | Impl Type | Source |
|---|---|---|---|---|---|---|
| **HQC-1** | i7-11850H, gcc 11.4 | 4557 kc | 9116 kc | 13918 kc | Reference C | HQC spec Table 7 |
| **HQC-1** | i7-11850H, gcc 8.2 | 76 kc | 150 kc | 353 kc | AVX2 | HQC spec Table 8 |
| **HQC-3** | i7-11850H, gcc 11.4 | 13783 kc | 27571 kc | 41669 kc | Reference C | HQC spec Table 7 |
| **HQC-3** | i7-11850H, gcc 8.2 | 181 kc | 355 kc | 732 kc | AVX2 | HQC spec Table 8 |
| **Aigis-enc I** | i7-6700, Win10 | 24686 cyc | 35535 cyc | 31540 cyc | AVX2 | Aigis-enc doc Table 2 |
| **Aigis-enc II** | i7-6700, Win10 | 34456 cyc | 49740 cyc | 44745 cyc | AVX2 | Aigis-enc doc Table 2 |
| **Aigis-enc III** | i7-6700, Win10 | 46291 cyc | 62087 cyc | 60153 cyc | AVX2 | Aigis-enc doc Table 2 |
| **Scloud+-128** | i9-10980XE, gcc 7.2 | 1052 kc | 1115 kc | 1109 kc | Optimized C | Scloud+ Table 5 |
| **Scloud+-192** | i9-10980XE, gcc 7.2 | 2034 kc | 2226 kc | 2262 kc | Optimized C | Scloud+ Table 5 |
| **Scloud+-256** | i9-10980XE, gcc 7.2 | 3564 kc | 3738 kc | 3884 kc | Optimized C | Scloud+ Table 5 |
| **CTRU/CNTR** | i7-10510U, gcc 9.4 | TODO | TODO | TODO | — | CTRU paper (待补) |
| **NEV** | (awaiting extraction) | TODO | TODO | TODO | — | NEV paper (待补) |

kc = kilo-cycles. cyc = cycles. Different CPUs and compilers → NOT comparable across rows.

### Signature Software Benchmarks

| Algorithm | Platform | KeyGen | Sign | Verify | Impl Type | Source |
|---|---|---|---|---|---|---|
| **Aigis-sig I** | i7-6700, Win10 | 75216 cyc | 296716 cyc | 78841 cyc | AVX2 | Aigis-sig doc Table 2 |
| **Aigis-sig II** | i7-6700, Win10 | 112362 cyc | 459903 cyc | 104337 cyc | AVX2 | Aigis-sig doc Table 2 |
| **Aigis-sig II-b** | i7-6700, Win10 | 102852 cyc | 624031 cyc | 104488 cyc | AVX2 | Aigis-sig doc Table 2 |
| **Aigis-sig III** | i7-6700, Win10 | 140563 cyc | 533880 cyc | 136503 cyc | AVX2 | Aigis-sig doc Table 2 |
| **UOV uov-Ip** | Xeon E3-1230L (Haswell) | 3243 kc | 115 kc | 103 kc | AVX2 | UOV spec Table 2 |
| **UOV uov-V** | Xeon E3-1230L (Haswell) | 62045 kc | 656 kc | 620 kc | AVX2 | UOV spec Table 2 |

---

## Round 3 Candidates — Compact Summary

For full parameter tables, see `database/metadata/additional_signatures_round3_tables.md`.

| Candidate | Best pk (B) | Best sig (B) | Best pk+sig | NIST Levels | Trade-off summary |
|---|---|---|---|---|---|
| **FAEST** | 32 | 3906 | 3938 | I/III/V | Tiny pk, large sig; only needs AES |
| **HAWK** | 450 | 249 | 1579 (512) | I/V (challenge) | Balanced; complex implementation |
| **MAYO** | 1420 | 186 | 5098 (MAYO2) | 1/3/5 | Good pk-sig tradeoff; multivariate |
| **MQOM** | 52 | 2820 | 3220 (gf2-short) | I/III/V | Small pk; moderate-large sig |
| **QR-UOV** | 12266 | 157 | 35507 (31,ell=3) | I/III/V | Moderate sigs; large pks |
| **SDitH** | 70 | 3661 | 3771 (gf256-short) | I/III/V | Small pk; code-based diversity |
| **SNOVA** | 1016 | 124 | 1264 (l=4,L1) | I/III/V | Best pk+sig among MV candidates |
| **SQIsign** | 65 | 148 | 213 (NIST-I) | I/III/V | **Smallest overall**; extremely complex |
| **UOV** | 43576 | 96 | 66576 (uov-Is) | 1/3/5 | Smallest sig (96B); huge pk |

---

## Quick Reference: "Which is smallest/largest?"

| Metric | KEM Winner | KEM Value | Sig Winner | Sig Value |
|---|---|---|---|---|
| 🏆 Smallest pk | ML-KEM-512 / CTRU-Light | 800B / 640B | SLH-DSA / SQIsign | 32B / 65B |
| 🏆 Smallest ct/sig | NEV-512 / CTRU-Light | 615B / 512B | UOV uov-Is / SQIsign | 96B / 148B |
| 🏆 Smallest total bandwidth | CTRU-Light | 1152B | SQIsign NIST-I | 213B |
| 🏆 Smallest total (standard only) | ML-KEM-512 | 1568B | Falcon-512 | 1563B |
| 💣 Largest pk | Scloud+-256 | 18744B | UOV uov-V | 447KB |
| 💣 Largest ct/sig | HQC-5 | 14421B | SLH-DSA-256f | 49856B |
| 💣 Largest total | Scloud+-256 | 35660B | UOV uov-V | ~447KB |

---

## Agent Usage

When asked for cross-algorithm comparison:

1. First narrow the scope: KEM only? Signature only? Both? Specific security level?
2. Use this file's tables for the high-level comparison.
3. For exact parameters, reference `parameter_tables.md`, `parameter_tables_extended.md`, or `additional_signatures_round3_tables.md`.
4. Always note standardization status differences — don't put ✅ FIPS algorithms next to 🔷 candidates without the status column.
5. For performance comparisons, always state platform and measurement differences — never claim "X is faster than Y" from these tables alone.
