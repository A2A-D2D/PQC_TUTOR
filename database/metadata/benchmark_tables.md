# Hardware Benchmark Tables

Rule: benchmark data is the highest-risk hallucination zone. Do not provide exact area, latency, frequency, power, LUT/FF/DSP/BRAM, or ranking unless a row in this file or a cited paper table supports it.

**Last updated:** 2026-06-23
**Data sources:** Falcon hardware papers, NTRU-NTT design documents
**Data gaps:** ML-KEM, ML-DSA, SLH-DSA FPGA/ASIC data NOT in this corpus. HQC hardware data NOT in this corpus. China-algorithm synthesis results NOT in this corpus.

---

## Falcon / FN-DSA — Full Hardware Implementation (FPGA)

Source: Schmid et al., "Falcon Takes Off – A Hardware Implementation of the Falcon Signature Scheme", 2023.
Platform: Xilinx Zynq UltraScale+ ZCU104, High-Level Synthesis (HLS) from C reference code.

### Falcon-512 (NIST Level 1)

| Function | BRAM | DSP | FF | LUT | Clock Cycles | Latency (ms) | Max MHz | Source |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| **sign_tree** | 32 | 182 | 44,249 | 46,971 | 787,441 | 4.2 | 187.5 | Table 1 |
| **key_gen** | 56 | 1,209 | 91,615 | 98,752 | — | 113.7 (±22.2) | 100.0 | Table 1 |
| **expand_pk** | 23 | 101 | 26,083 | 22,469 | 544,153 | 2.5 | 214.3 | Table 1 |
| **verify** | 13 | 15 | 8,078 | 11,544 | 132,482 | 0.6 | 214.3 | Table 1 |

### Falcon-1024 (NIST Level 5)

| Function | BRAM | DSP | FF | LUT | Clock Cycles | Latency (ms) | Max MHz | Source |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| **sign_tree** | 37 | 182 | 41,370 | 45,223 | 1,638,253 | 8.7 | 187.5 | Table 1 |
| **key_gen** | 69 | 1,215 | 91,029 | 100,649 | — | 320.3 (±69.1) | 100.0 | Table 1 |
| **expand_pk** | 29 | 139 | 30,703 | 27,666 | 1,191,337 | 5.6 | 214.3 | Table 1 |
| **verify** | 14 | 15 | 8,619 | 13,302 | 269,608 | 1.3 | 214.3 | Table 1 |

**Agent notes:**
- sign_tree and verify numbers include message hashing (50-byte short message).
- key_gen latency depends on a random seed; only measured latency (with std dev) is given, not exact cycle counts.
- These are HLS-generated results, not hand-optimized RTL. Hand-crafted HDL would likely achieve better area/latency.
- This is the **only** published full-hardware Falcon implementation in this corpus (sign + keygen).

---

## Falcon / FN-DSA — NTT/FFT Accelerators (ASIC)

### Efficient NTT/INTT Processor

Source: Dam et al., "Efficient NTT/INTT Processor for FALCON Post-Quantum Cryptography", 2025.

| Metric | Value | Notes |
|---|---|---|
| **Process** | Global Foundries 22nm FD-SOI | Standard cell ASIC |
| **Area** | 0.04 mm² | NTT/INTT core only |
| **Power** | 18.2 mW | @ 1 GHz |
| **Frequency** | 1 GHz | |
| **vs. ARM Cortex-M4** | 700× more energy efficient | |
| **vs. ARM Cortex-M4** | 200× faster | |
| **Area·Time product** | Lowest among compared works | |
| **Key feature** | Montgomery multipliers optimized for ASIC | |
| Source | Abstract, Section I | |

### Area and Power Efficient FFT/IFFT Processor

Source: "Area and Power Efficient FFT/IFFT Processor for FALCON Post-Quantum Cryptography", 2025.

| Metric | Value | Notes |
|---|---|---|
| **Process** | Global Foundries 22nm | ASIC |
| **Area** | 0.15 mm² | FFT/IFFT only |
| **Power** | 12.6 mW | @ 167 MHz |
| **Frequency** | 167 MHz | |
| **vs. classic FFT processors** | 42% less area | Normalized comparison |
| **vs. classic FFT processors** | 83% less power | |
| **Memory** | 4 KB (reduced from 28 KB) | No BRAM in ASIC context |
| Source | Abstract, Section I | |

### Unified FFT/NTT Design

Source: "A Unified FFT/NTT Design for Efficient NTRU Equation Solving in FALCON Cryptography", 2025.

| Metric | Value | Notes |
|---|---|---|
| **Process** | 40nm | ASIC |
| **Area** | 0.54 mm² | Combined FFT + NTT |
| **Frequency** | 333 MHz | |
| **Key feature** | Single hardware supporting both FFT (64-bit radix-4) and NTT (128-bit radix-2) | |
| **FFT+NTT share** | 26% + 18% = 44% of total KeyGen cycles | Motivation for unified design |
| Source | Abstract, Section I | |

---

## Falcon / FN-DSA — Sub-Module Accelerators

### Compact FFT/NTT FPGA Accelerator

Source: Dam et al., "Compact FALCON FFT/NTT Accelerator for Post-Quantum Cryptography", ISCAS 2025.

| Metric | Value | Notes |
|---|---|---|
| **Platform** | FPGA | |
| **512-point FFT** | 2,048 clock cycles | |
| **1024-point FFT** | 4,608 clock cycles | |
| **DSP usage** | 20 DSPs | Toom-3 algorithm reduces from 36 → 20 for complex FP64 multiplication |
| **BRAM usage** | 4 BRAMs (64×512) | Sufficient for all FALCON coefficient sizes |
| **Architecture** | 8 radix-2 butterfly units in parallel | |
| **vs. ASIC [22]** | 2× faster FFT (2 BUs vs 1 BU) | |
| **Limitation** | NTT support not described in abstract | |
| Source | Abstract, Sections I, III | |

### Discrete Gaussian Sampling HW/SW Co-Design

Source: Karabulut and Aysu, "A Hardware-Software Co-Design for the Discrete Gaussian Sampling of FALCON Digital Signature", 2025.

| Metric | Value | Notes |
|---|---|---|
| **Platform** | Xilinx Zynq SoC (ARM Cortex-A9 + FPGA) | |
| **Sampling acceleration** | 9.83× over reference software | |
| **Sampling share of signing** | 72% of total signature generation time | Motivation for acceleration |
| **Design feature** | Fully-pipelined datapath, parameterized area/performance trade-off | |
| **Flexibility** | Variable means and variances supported in hardware | Unique requirement of FALCON sampling |
| Source | Abstract, Section I | |

---

## PQC NTT Unified Architecture (Design Document)

Source: `PQC-NTT设计/pqc-ntt-parameter-resource-design.pdf` (internal design document).

This is an architectural design document, NOT synthesis results. Included here for hardware architecture reference.

### Supported Moduli and Algorithms

| Modulus | Value | Algorithms | Coefficient bit width |
|---|---|---|---|
| MOD_NEV | 769 | NEV / NEV' | 10 bit |
| MOD_CTRU | 3457 | CTRU / CNTR | 12 bit |
| MOD_FALCON | 12289 | Falcon verify | 14 bit |
| MOD_HAWK_AUX | 18433 | HAWK NTT | 15 bit |
| MOD_Q2 | 2^10 / 2^11 | CTRU/CNTR q2 | special path (no NTT) |

### Architecture Summary

| Feature | Specification |
|---|---|
| **Memory interface** | 256-bit shared memory port |
| **KEM datapath** | 16 lanes × 16 bit (NTT) |
| **DSA datapath** | 8 lanes × 32 bit (NTT, repackable to 16×16) |
| **NTT sizes supported** | N256 (HAWK-256), N512, N768 (mixed-radix), N1024 |
| **Ring modes** | x^n+1 (NEV/Falcon/HAWK), x^n-x^(n/2)+1 (CTRU/CNTR) |
| **Transform modes** | FULL_NTT, MIXED_RADIX_NTT, PNTT (NEV segmented), AUX_NTT (HAWK), Q2_SPECIAL |
| **Tail operations** | E8 decode, vector vote, norm check, Q-norm check |

**Agent note:** This document describes a unified NTT hardware architecture but does NOT include synthesis results (no LUT/FF/DSP/BRAM/frequency numbers). Use for architecture discussion only.

---

## NTRU Family Algorithm Implementation Analysis

Source: `NTRU-NTT设计/NTRU家族算法实现分析.pdf` (internal analysis document).

This document analyzes the algorithm flows for CTRU, CNTR, NEV, NEV', Falcon, and HAWK from a hardware implementation perspective. It covers:
- Algorithm pseudocode for KeyGen, Enc(aps), Dec(aps), Sign, Verify
- Identification of common operations (NTT, point-wise multiplication, polynomial encoding/decoding)
- NTT dataflow patterns

**No synthesis/benchmark numbers are provided in this document.**

---

## Summary: What's Available and What's Missing

### ✅ Available in this database

| Algorithm | Data type | Detail level |
|---|---|---|
| Falcon-512/1024 | Full FPGA (Zynq US+) | LUT, FF, DSP, BRAM, cycles, latency, MHz for all 4 functions |
| Falcon NTT/INTT | ASIC (GF 22nm) | Area, power, frequency, energy efficiency |
| Falcon FFT/IFFT | ASIC (GF 22nm) | Area, power, frequency, comparison |
| Falcon FFT/NTT | ASIC (40nm) | Area, frequency, unified design |
| Falcon FFT/NTT | FPGA | Cycles, DSP, BRAM for compact accelerator |
| Falcon Gaussian sampling | FPGA SoC | Acceleration factor, pipeline design |
| PQC NTT unified arch | Architecture doc | Moduli, modes, datapath specs (no synthesis) |

### ❌ NOT in this corpus (requires external sources)

| Missing data | Why it matters |
|---|---|
| **ML-KEM FPGA/ASIC** | Most important KEM standard — hardware data essential |
| **ML-DSA FPGA/ASIC** | Most important signature standard |
| **SLH-DSA FPGA/ASIC** | Hash-based alternative standard |
| **HQC FPGA/ASIC** | Code-based future standard |
| **CTRU/CNTR synthesis** | China KEM candidate hardware cost |
| **NEV synthesis** | Smallest-bandwidth KEM hardware cost |
| **Aigis-enc/sig synthesis** | China candidate hardware cost |
| **Scloud+ FPGA/ASIC** | Unstructured LWE hardware cost (large matrices) |
| **Any ASIC standard cell results** (except Falcon NTT sub-modules) | Comprehensive ASIC comparison |
| **Side-channel protected implementations** | Security vs. performance trade-off |

---

## Hardware Benchmark Entry Template

When adding new hardware results, use this template:

| Paper / source | Algorithm | Operation | Platform | Device / process node | Frequency | LUT | FF | DSP | BRAM | Area | Power | Latency cycles | Latency time | Memory included | Masking / protection | Result stage | Source table/section | Notes |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| (add rows) | | | | | | | | | | | | | | | | | | |

---

## Comparison Rules (repeated from v1)

When comparing hardware results, the agent must state at least:

1. algorithm and parameter set;
2. operation measured;
3. FPGA device or ASIC process;
4. frequency;
5. whether the number is cycles or time;
6. whether memory/SRAM/BRAM is included;
7. whether masking, shuffling, or side-channel protection is included;
8. whether the result is pre-synthesis, post-synthesis, post-place-and-route, silicon, or estimated.

**Never** compare numbers across different platforms, processes, or implementation methodologies without explicitly stating the differences.

## Unsafe Claims (do not make without source)

- "implementation A is faster than B"
- "this architecture is smaller"
- "this is the best hardware architecture"
- "candidate X is more efficient than candidate Y"
- "domestic algorithm X has lower area"
