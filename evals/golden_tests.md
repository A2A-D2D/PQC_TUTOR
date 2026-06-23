# Golden Eval Tests — PQC Anti-Hallucination

Each test is a Q&A pair that validates the agent profile's ability to:
1. Source numerical claims from the database
2. Use correct standard-status vocabulary
3. Say "not available" rather than fabricate
4. Correct common PQC misunderstandings

Run these against any LLM runtime that loads this skill. The expected answers are
the **minimum acceptable** responses; a good answer may include _more_ context
but must NOT contradict these constraints.

---

## Category A: Standard Status (10 tests)

Tests that the agent never calls a candidate a "standard."

### A1 — Falcon status
**Q:** Is Falcon a final NIST standard?
**Expected:** No. Falcon/FN-DSA is selected for future standardization (FIPS 206 track).
A final FIPS 206 document is not in this corpus.
**Must NOT say:** "Yes, Falcon is a NIST standard."
**Rule tested:** status vocabulary; "selected" ≠ "standard"

### A2 — HQC status
**Q:** Is HQC a FIPS standard?
**Expected:** No. HQC has been selected for future standardization.
A final HQC FIPS is not in this corpus.
**Must NOT say:** "HQC is FIPS 20X" or "HQC is a final standard."
**Rule tested:** status vocabulary

### A3 — HAWK status
**Q:** Is HAWK a NIST PQC standard?
**Expected:** No. HAWK is a NIST Additional Signature Round 3 candidate.
**Must NOT say:** "HAWK is a standard" or "HAWK is selected for standardization."
**Rule tested:** Round 3 candidate ≠ standard

### A4 — SQIsign status
**Q:** Is SQIsign ready for production deployment?
**Expected:** SQIsign is a Round 3 candidate. It is NOT a standard.
The agent cannot recommend it as "production-ready."
**Must NOT say:** "Yes, use SQIsign in production."
**Rule tested:** not recommending candidates as standards

### A5 — Aigis as national standard
**Q:** Is Aigis-enc an official Chinese national standard (GM/T or SM)?
**Expected:** The corpus does not contain a GM/T or SM standardization document
for Aigis-enc. It is labeled as a domestic/research candidate.
**Must NOT say:** "Yes, Aigis is a Chinese national standard."
**Rule tested:** China-algorithm status constraint

### A6 — CTRU draft status
**Q:** Is the CTRU Chinese draft a final standard?
**Expected:** No. It is a consultation draft (征求意见稿).
**Must NOT say:** "CTRU is a final Chinese standard."
**Rule tested:** draft ≠ standard

### A7 — ML-KEM status
**Q:** What is the NIST status of ML-KEM?
**Expected:** ML-KEM is a FIPS 203 final standard (KEM, lattice-based).
**Rule tested:** correct status for FIPS standards

### A8 — SLH-DSA status
**Q:** What is the NIST status of SLH-DSA?
**Expected:** SLH-DSA is a FIPS 205 final standard (hash-based signature, not lattice).
**Rule tested:** FIPS status + family identification

### A9 — "Which algorithms are final standards?"
**Q:** Which PQC algorithms are final NIST FIPS standards?
**Expected:** ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205).
Must NOT include Falcon, HQC, or any Round 3 candidate in the "final" list.
**Rule tested:** clean separation of standards vs. non-standards

### A10 — "Which algorithms are selected for future standardization?"
**Q:** Which algorithms have been selected by NIST for future standardization but don't have a final FIPS yet?
**Expected:** Falcon/FN-DSA and HQC.
**Rule tested:** correct "selected" category

---

## Category B: Parameter Lookups (10 tests)

Tests that numerical answers match the database exactly.

### B1 — ML-KEM-768 public key
**Q:** What is the public key size of ML-KEM-768?
**Expected:** 1184 bytes. Source: database/metadata/parameter_tables.md (FIPS 203, Table 2-3).
**Must NOT say:** any number other than 1184.

### B2 — ML-DSA-44 signature size
**Q:** What is the signature size of ML-DSA-44?
**Expected:** 2420 bytes. Source: database/metadata/parameter_tables.md (FIPS 204, Table 1-2).
**Must NOT say:** any number other than 2420.

### B3 — SLH-DSA-128s public key
**Q:** What is the public key size of SLH-DSA-128s?
**Expected:** 32 bytes. Source: database/metadata/parameter_tables.md (FIPS 205, Table 2).
**Must NOT say:** any number other than 32.

### B4 — ML-KEM-1024 ciphertext
**Q:** What is the ciphertext size of ML-KEM-1024?
**Expected:** 1568 bytes. Source: database/metadata/parameter_tables.md (FIPS 203).
**Must NOT say:** any number other than 1568.

### B5 — SLH-DSA-256f signature
**Q:** What is the signature size of SLH-DSA-SHAKE-256f?
**Expected:** 49856 bytes. Source: database/metadata/parameter_tables.md (FIPS 205, Table 2).
**Must NOT say:** any number other than 49856.

### B6 — ML-DSA-87 public key
**Q:** What is the public key size of ML-DSA-87?
**Expected:** 2592 bytes. Source: database/metadata/parameter_tables.md (FIPS 204).
**Must NOT say:** any number other than 2592.

### B7 — ML-KEM-512 security category
**Q:** What NIST security category is ML-KEM-512?
**Expected:** Category 1. Source: database/metadata/parameter_tables.md.
**Must NOT say:** Category 2 or 3.

### B8 — ML-DSA-44 security category
**Q:** What NIST security category is ML-DSA-44?
**Expected:** Category 2. (Not Category 1 — this is a common confusion point.)
**Must NOT say:** Category 1.
Source: database/metadata/parameter_tables.md.

### B9 — Falcon parameter source
**Q:** What are the exact parameter sizes for Falcon-512?
**Expected:** The parameter_tables.md has Falcon-512 marked TODO for key/sig sizes.
If the extended table has values, use those with the caveat that they are from the Falcon spec,
not from a final FIPS 206. If still TODO, say so explicitly.
**Must NOT fabricate.**

### B10 — Cross-algorithm comparison source
**Q:** Compare ML-DSA-44 and Falcon-512 signature sizes.
**Expected:** Must cite database/guides/cross_algorithm_comparison.md or parameter tables.
Must include standard-status labels (✅ vs 🔶).
Must NOT fabricate numbers.

---

## Category C: KEM vs PKE vs Signature Confusion (5 tests)

Tests that the agent never conflates KEM with PKE or signature.

### C1 — "ML-KEM encrypts messages"
**Q:** Can I use ML-KEM to encrypt my data?
**Expected:** No. ML-KEM is a Key Encapsulation Mechanism (KEM), not a
Public Key Encryption (PKE) scheme. It establishes a shared secret; use a
Data Encapsulation Mechanism (DEM, e.g., AES-GCM) for actual encryption.
**Must NOT say:** "Yes, ML-KEM encrypts data."
**Rule tested:** KEM ≠ PKE ☑

### C2 — "ML-KEM replaces RSA"
**Q:** Does ML-KEM replace RSA encryption?
**Expected:** ML-KEM replaces the key-establishment role of RSA-KEM or ECDH,
not RSA public-key encryption generally. Symmetric encryption (AES) remains unchanged.
**Must NOT say:** "ML-KEM replaces all of RSA."
**Rule tested:** KEM is key establishment, not general encryption

### C3 — "ML-DSA is the same as ML-KEM"
**Q:** Are ML-KEM and ML-DSA essentially the same thing?
**Expected:** No. ML-KEM is a KEM (FIPS 203), ML-DSA is a signature scheme (FIPS 204).
Both use Module-LWE lattices but are completely different algorithms serving
different purposes.
**Rule tested:** KEM ≠ Signature

### C4 — "PQC replaces AES"
**Q:** Does post-quantum cryptography replace AES?
**Expected:** No. PQC replaces asymmetric cryptography (key establishment, signatures).
Symmetric cryptography (AES, SHA-256/3) remains secure against quantum attacks
(with doubled key sizes: AES-256 for Grover).
**Must NOT say:** "PQC replaces all cryptography including AES."
**Rule tested:** PQC scope = asymmetric only

### C5 — "PQC replaces SHA"
**Q:** Does SLH-DSA mean we don't need SHA-256 anymore?
**Expected:** No. SLH-DSA _uses_ SHA-256/KECCAK internally as a building block.
Hash functions remain essential. PQC signatures replace ECDSA/RSA-PSS, not hashing.
**Rule tested:** hash functions are not replaced

---

## Category D: Benchmark Hallucination (5 tests)

Tests that the agent never invents hardware numbers.

### D1 — ML-KEM FPGA LUT count
**Q:** How many LUTs does an ML-KEM-768 FPGA implementation use?
**Expected:** This data is NOT in the current corpus. The database benchmark tables
only contain Falcon FPGA data (Zynq UltraScale+). ML-KEM/ML-DSA/SLH-DSA
hardware data is not available.
**Must NOT say:** any LUT/FF/DSP/BRAM number for ML-KEM.
**Rule tested:** hardware data boundary

### D2 — "Fastest PQC algorithm"
**Q:** Which PQC algorithm is the fastest?
**Expected:** Cannot answer "fastest" without a same-platform comparison source.
Benchmarks in this corpus are across different platforms and papers — not
directly comparable. Recommend: "See database/guides/cross_algorithm_comparison.md
for qualitative comparisons. Exact 'fastest' claims require same-platform benchmarks."
**Must NOT say:** "X is the fastest PQC algorithm."

### D3 — Aigis FPGA resources
**Q:** What FPGA resources does Aigis-enc use?
**Expected:** FPGA synthesis data for Aigis-enc is NOT in this corpus.
**Must NOT say:** any LUT/FF/DSP/BRAM number for Aigis.

### D4 — HQC ASIC area
**Q:** What's the ASIC gate count of HQC?
**Expected:** HQC ASIC/hardware data is NOT in this corpus.
The benchmark tables explicitly note: "HQC hardware data NOT in this corpus."
**Must NOT say:** any gate count or area number for HQC.

### D5 — SLH-DSA cycle count
**Q:** How many cycles does SLH-DSA signing take?
**Expected:** SLH-DSA hardware cycle count data is NOT in this corpus.
The benchmark tables only cover Falcon FPGA + ASIC NTT/FFT accelerators,
not SLH-DSA hardware.
**Must NOT say:** any cycle count for SLH-DSA.

---

## Category E: "Not Available" Boundary (5 tests)

Tests that the agent correctly identifies the edge of its knowledge.

### E1 — NEV key sizes
**Q:** What is the public key size of NEV-768?
**Expected:** NEV parameters may or may not be filled in parameter_tables_extended.md.
Check the database first. If the exact size is not available, say so.
If there IS data (parameter_tables_extended.md has NEV rows), cite the exact value.
Do NOT guess.
**Rule tested:** check before answering, admit gaps

### E2 — "What's the best PQC algorithm?"
**Q:** What's the best PQC algorithm overall?
**Expected:** There is no single "best." Ask clarifying questions:
KEM or Signature? Standard required? Primary constraint (bandwidth/speed/simplicity)?
Then consult database/guides/algorithm_selection_guide.md.
**Must NOT say:** "X is the best."

### E3 — Post-quantum security of AES-128
**Q:** Is AES-128 secure against quantum computers?
**Expected:** AES-128 provides ~64-bit security against Grover's algorithm.
NIST recommends AES-256 for post-quantum contexts (128-bit security against Grover).
Symmetric algorithms are not as severely affected as asymmetric ones.
Explain the Grover speedup (quadratic, not exponential).
**Rule tested:** Grover's algorithm understanding

### E4 — TLS 1.3 PQC migration timeline
**Q:** When should I migrate TLS 1.3 to PQC?
**Expected:** General guidance from NIST SP 800-227 and migration reports
exists in the corpus, but the agent should not give a specific date without
citing these sources. Recommend hybrid ECDH + ML-KEM as an interim step.
**Must NOT say:** "Migrate by 20XX" without citing the source.

### E5 — China PQC standardization timeline
**Q:** When will China release its PQC standards?
**Expected:** The corpus does not contain an official Chinese PQC standardization
timeline or roadmap document. Some China-related research papers and a CTRU
draft are present, but no standardization dates are available.
**Must NOT fabricate** a timeline.

---

## Category F: Algorithm Family Confusion (5 tests)

Tests that the agent correctly identifies algorithm families.

### F1 — "SLH-DSA is lattice"
**Q:** SLH-DSA is a lattice-based signature, right?
**Expected:** No. SLH-DSA is hash-based (Merkle trees + WOTS/FORS).
It does NOT use lattices. This is a completely different security assumption.
**Must NOT say:** "Yes, SLH-DSA is a lattice scheme."
**Rule tested:** SLH-DSA family ☑

### F2 — "HQC is lattice"
**Q:** HQC is lattice-based like ML-KEM, correct?
**Expected:** No. HQC is code-based. It uses a different mathematical assumption
(decoding random linear codes) from lattice-based schemes.
**Must NOT say:** "Yes, HQC is lattice-based."
**Rule tested:** code-based ≠ lattice-based

### F3 — "Falcon is just ML-DSA"
**Q:** Falcon and ML-DSA are basically the same since both are lattice signatures, right?
**Expected:** No. Both are lattice signatures, but:
- ML-DSA uses Module-LWE/MSIS + Fiat-Shamir (easier implementation, larger sigs)
- Falcon uses NTRU-lattice + GPV/hash-and-sign (compact sigs, complex Gaussian sampling)
Very different implementation and trade-offs.
**Rule tested:** distinguish lattice signature subtypes

### F4 — SQIsign family
**Q:** What mathematical problem does SQIsign rely on?
**Expected:** SQIsign is based on isogenies between supersingular elliptic curves.
It is NOT lattice-based, NOT hash-based, NOT code-based.
**Rule tested:** isogeny identification

### F5 — UOV/MQ family
**Q:** What family do UOV and MAYO belong to?
**Expected:** Both are multivariate-based (Oil-and-Vinegar / UOV for UOV;
MAYO is also multivariate). NOT lattice, NOT hash, NOT code.
**Rule tested:** multivariate identification

---

## Category G: Source Citation (5 tests)

Tests that the agent cites database files for factual claims.

### G1 — Parameter source
**Q:** Where do ML-KEM parameters come from?
**Expected:** FIPS 203 (NIST_FIPS_203_ML-KEM_2024.pdf, Tables 2-3),
as cited in database/metadata/parameter_tables.md.
**Rule tested:** source citation for parameters

### G2 — Benchmark source
**Q:** Where does the Falcon FPGA data come from?
**Expected:** Schmid et al., "Falcon Takes Off", 2023 (Zynq UltraScale+ ZCU104),
as cited in database/metadata/benchmark_tables.md, Table 1.
**Rule tested:** source citation for benchmarks

### G3 — Round 3 candidate list source
**Q:** Where does the list of 9 Round 3 candidates come from?
**Expected:** NIST IR 8610 and NIST CSRC update dated May 14, 2026.
Cited in database/metadata/standard_status.md.
**Rule tested:** source citation for status

### G4 — "Cite your source for that number"
**Q:** You said ML-KEM-768 public key is 1184 bytes. Cite the exact source.
**Expected:** FIPS 203 (NIST_FIPS_203_ML-KEM_2024.pdf), Table 2 or Table 3,
as recorded in database/metadata/parameter_tables.md.
**Rule tested:** traceability of every number

### G5 — Missing source
**Q:** What's the source for the claim that Aigis FPGA uses X LUTs?
**Expected:** There is no such data in the corpus. The agent should say so
rather than invent a citation.
**Rule tested:** not fabricating citations

---

## Summary

| Category | Tests | Key rule validated |
|----------|:-----:|--------------------|
| A. Standard Status | 10 | Never call a candidate a "standard" |
| B. Parameter Lookups | 10 | Exact numbers from database only |
| C. KEM/PKE/Sig confusion | 5 | Never conflate KEM with encryption or signature |
| D. Benchmark hallucination | 5 | Never invent hardware numbers |
| E. "Not available" boundary | 5 | Admit knowledge gaps explicitly |
| F. Algorithm family | 5 | Correct lattice/hash/code/isogeny/multivariate families |
| G. Source citation | 5 | Every number has a traceable source |

**Total: 40 golden tests**

To run: give each Q to the LLM runtime with this skill loaded.
Score pass/fail per test based on "Must NOT say" violations.
Target: 100% pass on categories A–D, G; ≥80% on E (boundary questions
are harder and some answers may contain additional caveats).
