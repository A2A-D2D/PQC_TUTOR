# Extended Parameter Tables

Rule: numeric parameters in this file are copied from the PDFs in the current corpus, or explicitly marked as derived. Do not use this file to claim final standard status for schemes whose final standard is not present in the corpus.

## Falcon / FN-DSA-track

Source: `03_selected_future_standards/Falcon_specification_falcon-sign_2020.pdf`, Section 3.11.5 and Table 3.3.

Status note: Falcon is on the future-standard/FN-DSA track, but a final FIPS 206 document is not present in this corpus. Treat these values as Falcon specification values, not final FIPS 206 values.

| Parameter set | Type | Target NIST level in spec | Ring degree n | q | sigma | sigma_min | sigma_max | Max signature square norm floor(beta^2) | Public key bytes | Private key bytes | Signature bytes | Source note |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Falcon-512 | Signature | I | 512 | 12289 | 165.736617183 | 1.277833697 | 1.8205 | 34034726 | 897 | 1281 | 666 | pk/signature from Table 3.3; private key bytes derived from Sec. 3.11.5 fixed-width encoding: 1 + (2*n*6 + n*8)/8. |
| Falcon-1024 | Signature | V | 1024 | 12289 | 168.388571447 | 1.298280334 | 1.8205 | 70265242 | 1793 | 2305 | 1280 | pk/signature from Table 3.3; private key bytes derived from Sec. 3.11.5 fixed-width encoding: 1 + (2*n*5 + n*8)/8. |

Agent note: for a quickstart tutor, Falcon should be introduced as an NTRU-lattice GPV/hash-and-sign style signature scheme with fast Fourier sampling. Emphasize implementation complexity and compact signatures. Do not claim final FIPS 206 byte sizes unless a final FIPS 206 source is added.

## HQC

Source: `03_selected_future_standards/HQC_specification_2025-08-22.pdf`, Table 5 and Table 6.

Status note: HQC is selected for standardization, but a final FIPS document is not present in this corpus. Treat these as HQC specification values.

### HQC parameter sets

| Instance | Type | Security | n1 | n2 | n | k | omega | omega_r = omega_e | DFR |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| HQC-1 | KEM | NIST-1 | 46 | 384 | 17669 | 128 | 66 | 75 | < 2^-128 |
| HQC-3 | KEM | NIST-3 | 56 | 640 | 35851 | 192 | 100 | 114 | < 2^-192 |
| HQC-5 | KEM | NIST-5 | 90 | 640 | 57637 | 256 | 131 | 149 | < 2^-256 |

### HQC key and ciphertext sizes

| Instance | Security | Encapsulation key bytes ekKEM | Decapsulation key bytes dkKEM | Compressed dkKEM bytes | Ciphertext bytes cKEM | Shared key bytes K | Source note |
|---|---|---:|---:|---:|---:|---:|---|
| HQC-1 | NIST-1 | 2241 | 2321 | 32 | 4433 | 32 | Table 6; compressed dkKEM value follows the spec text describing the `seedKEM` compressed format. |
| HQC-3 | NIST-3 | 4514 | 4602 | 32 | 8978 | 32 | Table 6; compressed dkKEM value follows the spec text describing the `seedKEM` compressed format. |
| HQC-5 | NIST-5 | 7237 | 7333 | 32 | 14421 | 32 | Table 6; compressed dkKEM value follows the spec text describing the `seedKEM` compressed format. |

Agent note: introduce HQC as a code-based KEM relying on quasi-cyclic syndrome decoding, not as a lattice scheme. It is useful as an algorithmic-diversity complement to ML-KEM.

## Aigis-enc

Source: `05_china_related/Aigis-enc算法设计文档.pdf`, Table 1.

Status note: China-related design document. Do not present as a NIST/FIPS standard.

| Parameter set | Type | Target quantum security bits | Conservative classical security bits | n | k | q | eta1 | eta2 | dt | du | dv | Public key bytes | Secret key bytes | Compact secret key bytes | Ciphertext bytes | Shared secret bytes | DFR | Recommendation note |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| PARAMS I | KEM | 80 | 111 | 256 | 2 | 7681 | 2 | 12 | 10 | 9 | 3 | 672 | 928 | 32 | 672 | 32 | 2^-82 | Lower security set. |
| PARAMS II | KEM | 128 | 162 | 256 | 3 | 7681 | 1 | 4 | 9 | 9 | 4 | 896 | 1152 | 32 | 992 | 32 | 2^-128 | Document states this is the recommended parameter set. |
| PARAMS III | KEM | 192 | 235 | 512 | 2 | 12289 | 2 | 8 | 11 | 10 | 4 | 1472 | 1984 | 32 | 1536 | 64 | 2^-211 | Higher security set. |

Agent note: Aigis-enc is based on asymmetric MLWE/AMLWE design ideas. Keep this as domestic candidate/research context unless a formal standard source is added.

## Aigis-sig

Source: `05_china_related/Aigis-sig算法设计文档.pdf`, Table 1.

Status note: China-related design document. Do not present as a NIST/FIPS standard.

| Parameter set | Type | Target quantum security bits | Conservative classical security bits | n | k | l | q | d | omega | eta1 | eta2 | beta1 | beta2 | gamma1 | gamma2 | Public key bytes | Secret key bytes | Signature bytes | Expected Sign loop count | Recommendation note |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PARAMS I | Signature | 80 | 98 | 256 | 4 | 3 | 2021377 | 13 | 80 | 2 | 3 | 120 | 175 | 131072 | 168448 | 1056 | 2448 | 1852 | 5.86 | Lower security set. |
| PARAMS II | Signature | 128 | 141 | 256 | 5 | 4 | 3870721 | 14 | 96 | 2 | 5 | 120 | 275 | 131072 | 322560 | 1312 | 3376 | 2445 | 7.61 | Document states this is the recommended parameter set. |
| PARAMS II-b | Signature | 128 | 141 | 256 | 5 | 4 | 3870721 | 14 | 96 | 3 | 5 | 175 | 275 | 131072 | 322560 | 1312 | 3376 | 2445 | 11.7 | Alternative level-128 set. |
| PARAMS III | Signature | 160 | 178 | 256 | 6 | 5 | 3870721 | 14 | 120 | 1 | 5 | 60 | 275 | 131072 | 322560 | 1568 | 3888 | 3046 | 6.67 | Higher security set. |

Agent note: Aigis-sig is structurally close to Fiat-Shamir-with-aborts lattice signatures, with high/low bits and hints. In teaching mode, compare it with ML-DSA/Dilithium-style flow, but do not claim equivalence without source.

## Scloud+

Source: `05_china_related/Scloud+.pdf`, Table 2, Table 3, Table 4, and Table 6.

Status note: China-related research paper. Do not present as a NIST/FIPS standard.

### Scloud+ PKE/KEM parameters

| Parameter set | Type | lm = lss bits | q | q1 | q2 | m | n | mbar | nbar | h1 | h2 | eta1 | eta2 | Public key bytes | Ciphertext bytes | Shared secret bytes | Classical security bits (minimum in Table 4) | Quantum security bits (minimum in Table 4) | DFR |
|---|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Scloud+-128 | KEM | 128 | 2^12 | 2^9 | 2^7 | 600 | 600 | 8 | 8 | 150 | 150 | 7 | 7 | 7200 | 5456 | 16 | 136.07 | 123.49 | 2^-134.21 |
| Scloud+-192 | KEM | 192 | 2^12 | 2^12 | 2^10 | 928 | 896 | 8 | 8 | 224 | 232 | 2 | 1 | 11136 | 10832 | 24 | 200.42 | 183.65 | 2^-200.64 |
| Scloud+-256 | KEM | 256 | 2^12 | 2^10 | 2^7 | 1136 | 1120 | 12 | 11 | 280 | 284 | 3 | 2 | 18744 | 16916 | 32 | 263.11 | 242.21 | 2^-265.74 |

### Scloud+ MsgEnc / MsgDec parameters

| Parameter set | mu | tau | Coding lattice | Shaping lattice | Source |
|---|---:|---:|---|---|---|
| Scloud+-128 | 64 | 3 | BW32 | 8 * Z[i]^16 | Table 3 |
| Scloud+-192 | 96 | 4 | BW32 | 16 * Z[i]^16 | Table 3 |
| Scloud+-256 | 64 | 3 | BW32 | 8 * Z[i]^16 | Table 3 |

Agent note: Scloud+ is useful for explaining unstructured-LWE KEMs with lattice coding and BDD/MsgEnc/MsgDec. In hardware discussions, separate the paper's PKE/KEM parameters from any local RTL demo parameters.

## CTRU / CNTR research paper comparison

Source: `05_china_related/CTRU.pdf`, Table I.

Status note: research paper comparison table. Do not treat as an official standard. The separate Chinese draft below has different named parameter sets and should not be silently merged with this table.

| Scheme | Type | Assumptions | Ring | n | q | Public key bytes | Ciphertext bytes | Bandwidth bytes | Security bits (classical, quantum) | DFR |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| CTRU | KEM | NTRU, RLWE | Zq[x]/(x^n - x^(n/2) + 1) | 512 | 3457 | 768 | 640 | 1408 | (118,107) | 2^-143 |
| CTRU | KEM | NTRU, RLWE | Zq[x]/(x^n - x^(n/2) + 1) | 768 | 3457 | 1152 | 960 | 2112 | (181,164) | 2^-184 |
| CTRU | KEM | NTRU, RLWE | Zq[x]/(x^n - x^(n/2) + 1) | 1024 | 3457 | 1536 | 1408 | 2944 | (255,231) | 2^-195 |
| CNTR | KEM | NTRU, RLWR | Zq[x]/(x^n - x^(n/2) + 1) | 512 | 3457 | 768 | 640 | 1408 | (127,115) | 2^-170 |
| CNTR | KEM | NTRU, RLWR | Zq[x]/(x^n - x^(n/2) + 1) | 768 | 3457 | 1152 | 960 | 2112 | (191,173) | 2^-230 |
| CNTR | KEM | NTRU, RLWR | Zq[x]/(x^n - x^(n/2) + 1) | 1024 | 3457 | 1536 | 1280 | 2816 | (253,230) | 2^-291 |

## CTRU Chinese draft parameter sets

Source: `05_china_related/基于NTRU的密钥封装机制-征求意见稿.pdf`, Table 1, Table 2, and Table 3.

Status note: draft document in the corpus. Do not claim final GM/T standard status unless a final issued standard is added.

| Parameter set | Type | Ring family | n | n_prime | q | q2 | Psi1 | Psi2 | Secret key bytes | Public key bytes | Ciphertext bytes | Shared key bytes | Security bits (classical, quantum) | Source table |
|---|---|---|---:|---:|---:|---|---|---|---:|---:|---:|---:|---|---|
| CTRU-576 | KEM | Zq[x]/(x^n - x^(n/2) + 1) | 576 | 288 | 3457 | 2^10 | B4 | B4 | 1260 | 864 | 720 | 36 | (142,128) | Table 1 |
| CTRU-768 | KEM | Zq[x]/(x^n - x^(n/2) + 1) | 768 | 384 | 3457 | 2^10 | B3 | B3 | 1584 | 1152 | 960 | 48 | (192,173) | Table 1 |
| CTRU-1024 | KEM | Zq[x]/(x^n - x^(n/2) + 1) | 1024 | 512 | 3457 | 2^10 | B2 | B2 | 2112 | 1536 | 1280 | 64 | (255,231) | Table 1 |
| CTRU-Light | KEM | Zq[x]/(x^n + 1) | 512 | 256 | 769 | 2^8 | B1 | B1 | 864 | 640 | 512 | 32 | (125,114) | Table 2 |
| CTRU-Prime | KEM | Zq[x]/(x^n - x - 1) | 761 | 376 | 4591 | 2^10 | B2 | B2 | 1666 | 1237 | 952 | 48 | (173,157) | Table 3 |

Agent note: keep the research-paper CTRU/CNTR table and the Chinese draft CTRU parameter table separate. They use different named parameter sets and sometimes different n values.

## NEV

Source: `05_china_related/NEV.pdf`, Table 1.

Status note: research paper. Do not present as a standard or NIST candidate unless a status source is added.

| Scheme | Type | Intended security context in paper | Public key bytes | Secret key bytes | Ciphertext bytes | DFR | LWE estimator bits | Notes |
|---|---|---|---:|---:|---:|---|---:|---|
| NEV-512 | KEM/PKE-derived KEM | NIST level 1 context | 615 | 1294 | 615 | 2^-138 | 141 | Table 1 comparison row. |
| NEV'-512 | Optimized NEV variant | NIST level 1 context | 615 | 1294 | 615 | 2^-200 | 145 | Table 1 comparison row; relies on additional sspRLWE-style assumption discussion in paper. |
| NEV-1024 | KEM/PKE-derived KEM | NIST level 5 context | 1229 | 2522 | 1229 | 2^-152 | 281 | Table 1 comparison row. |
| NEV'-1024 | Optimized NEV variant | NIST level 5 context | 1229 | 2522 | 1229 | 2^-200 | 292 | Table 1 comparison row; relies on additional sspRLWE-style assumption discussion in paper. |

Agent note: NEV is best used as a research example of NTRU-style encryption/KEM with vector decoding. It is not a replacement for ML-KEM in standards teaching.

## Additional-signature Round 3 candidates

Source: PDFs under `04_nist_additional_signatures_round3/` and NIST status reports under `02_nist_reports_migration/`.

Full parameter tables with exact key/signature sizes and all parameter sets: **`database/metadata/additional_signatures_round3_tables.md`**.

All values below verified against source PDFs on 2026-06-23.

### Summary index with size ranges

| Candidate | Family | Sets | pk range (bytes) | sig range (bytes) | Status |
|---|---|---|---|---|---|
| FAEST | Symmetric (AES/Rijndael OWF + VOLEitH) | 12 (6 FAEST + 6 FAEST-EM) | 32 – 64 | 3906 – 26548 | ✅ |
| HAWK | Lattice (NTRU hash-and-sign) | 3 (incl. 1 challenge) | 450 – 2440 | 249 – 1221 | ✅ |
| MAYO | Multivariate (whipped OV) | 4 (MAYO1/2/3/5) | 1420 – 5554 (compact) | 186 – 964 | ✅ |
| MQOM | Multivariate (MQ + MPCitH) | 12 (GF2/GF256 × short/fast) | 52 – 160 | 2820 – 17444 | ✅ |
| QR-UOV | Multivariate (quotient-ring UOV) | 12 (3 recommended + 9 additional) | 12266 – 173676 | 157 – 807 | ✅ |
| SDitH | Code-based (syndrome decoding itH) | 18 (GF2/GF256/TCitH variants) | 70 – 152 | 3661 – 19968 | ✅ |
| SNOVA | Multivariate (structured UOV/rings) | 11 (l=2/3/4/5 × L1/L3/L5) | 1016 – 71890 | 124 – 576 | ✅ |
| SQIsign | Isogeny-based | 3 (NIST-I/III/V) | 65 – 129 | 148 – 292 | ✅ |
| UOV | Multivariate (unbalanced OV) | 4 (uov-Ip/Is/III/V) | 43576 – 446992 (compact) | 96 – 260 | ✅ |

### Source file index with verification

| Candidate | Source PDF | Key table(s) | Verified |
|---|---|---|---|
| FAEST | `04_nist_additional_signatures_round3/FAEST_v2_specification_2025.pdf` | Table 3.1 | ✅ 2026-06-23 |
| HAWK | `04_nist_additional_signatures_round3/HAWK_v1.1_specification.pdf` | Table 2, Table 4 | ✅ 2026-06-23 |
| MAYO | `04_nist_additional_signatures_round3/MAYO_round2_specification_2025.pdf` | Table 2.1 | ✅ 2026-06-23 |
| MQOM | `04_nist_additional_signatures_round3/MQOM_round2_specification_2025.pdf` | Table 6, Table 7 | ✅ 2026-06-23 |
| QR-UOV | `04_nist_additional_signatures_round3/QR-UOV_v2.0_specification_2025.pdf` | Tables 1-5 | ✅ 2026-06-23 |
| SDitH | `04_nist_additional_signatures_round3/SDitH_round2_specification_2025.pdf` | Tables 3-9 | ✅ 2026-06-23 |
| SNOVA | `04_nist_additional_signatures_round3/SNOVA_round2_specification_2025.pdf` | Table 6 | ✅ 2026-06-23 |
| SQIsign | `04_nist_additional_signatures_round3/SQIsign_v2.0.1_specification_2025.pdf` | Table 4 | ✅ 2026-06-23 |
| UOV | `04_nist_additional_signatures_round3/UOV_round2_specification_2025.pdf` | Table 4 (Table 1 in PDF) | ✅ 2026-06-23 |

Agent note: these are Round 3 candidate specification values, not final FIPS standard values. Do not give deployment recommendations or “best candidate” claims from size tables alone. For full details (all parameter rows, teaching notes, family groupings), read `additional_signatures_round3_tables.md`.
