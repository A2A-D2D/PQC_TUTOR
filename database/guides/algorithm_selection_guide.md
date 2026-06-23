# PQC Algorithm Selection Guide — 后量子密码算法选型指南

This guide helps engineers and architects choose a PQC algorithm based on their use case, constraints, and risk tolerance. All recommendations reference the database parameter tables. **Always check `standard_status.md` for the latest standardization status before making a final decision.**

---

## Quick Selection (30 seconds)

**"I just need a safe default today."**

| If you need... | Pick... | Why |
|---|---|---|
| Key establishment (like ECDH) | **ML-KEM-768** | Final NIST standard (FIPS 203), balanced security/performance |
| Digital signatures (like ECDSA) | **ML-DSA-65** | Final NIST standard (FIPS 204), easiest lattice signature to implement |
| Conservative backup KEM | **HQC-3** | Code-based (different math from lattices), selected for future standard |
| Conservative backup signature | **SLH-DSA-192s** | Hash-based (no lattice assumption), final NIST standard (FIPS 205) |
| Compact signatures | **Falcon-512** | ~2.7x smaller sigs than ML-DSA, future-standard track (FN-DSA) |

---

## Decision Flow

### Step 1: What primitive do you need?

```
需要什么密码原语？
├── 🔑 Key Establishment / KEM (替代 ECDH)
│   └── 继续 → Step 2A
├── ✍️ Digital Signature (替代 ECDSA / RSA-PSS)
│   └── 继续 → Step 2B
└── 🔐 Both
    ├── 先分别选择 KEM 和 Signature
    └── 然后考虑 hybrid mode 组合
```

---

### Step 2A: KEM Selection

```
需要 KEM
├── 🏛️ 必须用已发布的标准？
│   ├── YES → ML-KEM (FIPS 203)
│   │   ├── NIST Level 1 (128-bit) → ML-KEM-512
│   │   ├── NIST Level 3 (192-bit) → ML-KEM-768  ← 推荐
│   │   └── NIST Level 5 (256-bit) → ML-KEM-1024
│   │
│   └── NO / 可以等 →
│       ├── 想要算法多样性（非格）？
│       │   └── HQC (code-based, selected for future standard)
│       │       ├── NIST-1 → HQC-1
│       │       ├── NIST-3 → HQC-3
│       │       └── NIST-5 → HQC-5
│       │
│       ├── 想要无代数结构（最保守）？
│       │   └── Scloud+ (unstructured LWE, research)
│       │       注意: pk/ct 较大 (7KB~19KB)，性能低于 ML-KEM
│       │
│       └── 中国国内场景？
│           ├── CTRU-768 (征求意见稿, NTRU+RLWE)
│           ├── Aigis-enc PARAMS II (AMLWE, 推荐参数集)
│           └── NEV-512 / NEV'-512 (NTRU+vector decoding)
```

**KEM 快速对比 (NIST Level 3 / 128-bit 等效):**

| 算法 | 标准状态 | pk (B) | ct (B) | 总带宽 | 实现难度 |
|------|------|------|------|------|------|
| **ML-KEM-768** | ✅ FIPS 203 | 1184 | 1088 | 2272 | ⭐⭐ 中等 |
| HQC-3 | 🔶 未来标准 | 4514 | 8978 | 13492 | ⭐⭐⭐ 较高 |
| Scloud+-128 | 🔷 研究 | 7200 | 5456 | 12656 | ⭐⭐ 中等 |
| CTRU-768 (草案) | 🔷 草案 | 1152 | 960 | 2112 | ⭐⭐ 中等 |
| Aigis-enc II | 🔷 研究 | 896 | 992 | 1888 | ⭐⭐ 中等 |
| NEV-512 | 🔷 研究 | 615 | 615 | 1230 | ⭐⭐ 中等 |

---

### Step 2B: Signature Selection

```
需要 Digital Signature
├── 🏛️ 必须用已发布的标准？
│   ├── YES →
│   │   ├── 实现最简单 → ML-DSA (FIPS 204)
│   │   │   ├── NIST Level 2 → ML-DSA-44
│   │   │   ├── NIST Level 3 → ML-DSA-65  ← 推荐
│   │   │   └── NIST Level 5 → ML-DSA-87
│   │   │
│   │   └── 最保守假设 → SLH-DSA (FIPS 205, hash-based)
│   │       ├── 小签名优先 → SLH-DSA-*-s (如 128s: 7.8KB)
│   │       └── 快验证优先 → SLH-DSA-*-f (如 128f: 17KB)
│   │
│   └── NO / 可以接受未来标准 →
│       ├── 想要最小签名？
│       │   ├── Falcon-512 (666B) / Falcon-1024 (1280B) — 未来标准
│       │   ├── SQIsign NIST-I (148B) — Round 3 候选, 同源密码
│       │   └── UOV uov-Is (96B) — Round 3 候选, 但 pk 很大 (66KB)
│       │
│       ├── 想要最小公钥 + 小签名？
│       │   ├── HAWK-512 (pk=1024B, sig=555B) — Round 3 候选
│       │   └── SQIsign NIST-I (pk=65B, sig=148B) — 极小, 但实现极复杂
│       │
│       ├── 想要多变量方案的多样性？
│       │   ├── MAYO2 (pk=4.9KB, sig=186B) — 小签名
│       │   └── SNOVA l=4 (pk=1KB, sig=248B) — 小公钥
│       │
│       ├── 想要编码-based 的多样性？
│       │   └── SDitH — 各种参数集可选
│       │
│       └── 中国国内场景？
│           ├── Aigis-sig PARAMS II (推荐, AMLWE+AMSIS)
│           └── HAWK (NTRU-style, Round 3)
```

**Signature 快速对比 (NIST Level 1-3 / 128-bit 等效):**

| 算法 | 标准状态 | pk | sig | 签名速度 | 实现难度 |
|------|------|------|------|------|------|
| **ML-DSA-44** (L2) | ✅ FIPS 204 | 1312 | 2420 | ⭐⭐⭐ 快 | ⭐⭐ 中等 |
| **ML-DSA-65** (L3) | ✅ FIPS 204 | 1952 | 3309 | ⭐⭐⭐ 快 | ⭐⭐ 中等 |
| SLH-DSA-128s | ✅ FIPS 205 | 32 | 7856 | ⭐ 慢 | ⭐⭐ 中等 |
| **Falcon-512** | 🔶 未来标准 | 897 | 666 | ⭐⭐ 中 | ⭐⭐⭐⭐ 难 |
| HAWK-512 | 🔷 候选 | 1024 | 555 | ⭐⭐ 中 | ⭐⭐⭐⭐ 难 |
| SQIsign NIST-I | 🔷 候选 | 65 | 148 | ⭐ 慢 | ⭐⭐⭐⭐⭐ 极难 |
| Aigis-sig II | 🔷 研究 | 1312 | 2445 | ⭐⭐⭐ 快 | ⭐⭐ 中等 |

---

## Constraint-Based Selection Matrix

### "我主要关心带宽"

| 约束 | KEM 推荐 | Signature 推荐 |
|------|------|------|
| 最小总带宽 (pk+ct) | NEV-512 (1230B) / Aigis-enc II (1888B) | — |
| 最小签名 | — | SQIsign NIST-I (148B) / UOV uov-Is (96B ⚠️ pk=66KB) |
| 最小公钥 (sig) | — | SLH-DSA (32B) / SQIsign NIST-I (65B) |
| 最小 pk+sig 组合 | — | Falcon-512 (897+666=1563B) |
| 标准内最小带宽 | ML-KEM-512 (1568B) | Falcon-512 (1563B, 未来标准) |

### "我主要关心里面面积/硬件成本"

| 约束 | KEM 推荐 | Signature 推荐 |
|------|------|------|
| 无 NTT（省面积） | HQC（编码, 无NTT） / Scloud+（非结构化LWE） | SLH-DSA（纯hash） |
| 最小模块复用 | ML-KEM ≈ ML-DSA（共享 NTT + Keccak） | ML-DSA（与ML-KEM共享NTT） |
| 最简单控制逻辑 | SLH-DSA（主要是hash） | SLH-DSA |

### "我主要关心安全性"

| 约束 | KEM 推荐 | Signature 推荐 |
|------|------|------|
| 最保守假设 | Scloud+（无代数结构LWE） | SLH-DSA（仅靠hash函数安全性） |
| 算法多样性（防格被攻破） | HQC（编码, 非格） | SLH-DSA（hash, 非格） + SQIsign（同源） |
| 中国国内合规 | CTRU / Aigis-enc | Aigis-sig |

### "我不想踩坑（最简单实现）"

| 约束 | KEM 推荐 | Signature 推荐 |
|------|------|------|
| 参考实现最成熟 | ML-KEM（NIST + liboqs + 大量开源） | ML-DSA（同上） |
| 最少实现陷阱 | ML-KEM | ML-DSA |
| 避免浮点/高斯采样 | ML-KEM / ML-DSA | ML-DSA / SLH-DSA（避免 Falcon 的复杂采样） |

---

## Role-Based Recommendations

### 🎓 PQC 初学者
**目标：** 快速建立正确的PQC心智模型

- 先学 **ML-KEM-768** — 理解 KEM ≠ PKE ≠ 加密
- 再学 **ML-DSA-65** — 理解 Fiat-Shamir with Aborts
- 然后对比 **Falcon-512** — 理解同一家族内的设计取舍
- 最后看 **SLH-DSA** — 理解"不需要格"的签名

### 💻 软件开发/集成工程师
**目标：** 把 PQC 集成到 TLS/SSH/VPN 中

- 首选 **ML-KEM-768 + ML-DSA-65** — 都是 FIPS 标准，liboqs 有成熟实现
- Hybrid mode: **X25519 + ML-KEM-768**（参考 OpenSSH 9.0+ 做法）
- 如需保守备份: 加上 **SLH-DSA-128s** 作为第二签名
- 关注: key size 对协议消息大小的影响、certificate chain 适配

### 🔧 硬件/FPGA 工程师
**目标：** 在 FPGA/ASIC 上高效实现 PQC

- 优先考虑 **ML-KEM + ML-DSA** 组合 — 共享 Keccak + NTT 硬件模块
- 面积敏感 → **SLH-DSA**（纯 hash，无 NTT/DSP）
- 研究参考: 查看 `database/implementation/pqc_hardware_modules.md`
- 性能数据: 查看 `database/metadata/software_benchmark_tables.md`（软件参考）
- ⚠️ Hardware benchmark 表目前为空，需要从论文中补充

### 🏛️ 安全架构师
**目标：** 为组织制定PQC迁移策略

- 当前部署: **ML-KEM-768 + ML-DSA-65**（FIPS 标准，合规无忧）
- Hybrid transition: ECDH + ML-KEM / ECDSA + ML-DSA
- 长期备份: **HQC + SLH-DSA**（不同数学假设）
- 跟踪: Falcon/FN-DSA（FIPS 206 发布后加入）
- 时间线: 参考 `02_nist_reports_migration/` 中的迁移指南

### 🇨🇳 中国PQC研究者
**目标：** 了解国内算法格局

- KEM 候选: **CTRU-768**（征求意见稿）、**Aigis-enc II**（推荐参数）
- 签名候选: **Aigis-sig II**（推荐参数）
- 非结构化方案: **Scloud+**（无环/模结构，保守选择）
- 研究参考: **NEV**（vector decoding 技术）
- ⚠️ 所有中国算法标记为 "研究/国内候选"，不声称 GM/T 或 SM 标准状态

---

## Algorithm Family Map

```
PQC Algorithms
├── 🥇 Final NIST Standards (可立即部署)
│   ├── ML-KEM (FIPS 203) — 格 KEM
│   ├── ML-DSA (FIPS 204) — 格 签名
│   └── SLH-DSA (FIPS 205) — Hash 签名
│
├── 🥈 Selected Future Standards (2-3年内预计发布)
│   ├── Falcon / FN-DSA (FIPS 206) — 格 签名 (紧凑)
│   └── HQC — 编码 KEM (多样性)
│
├── 🥉 Round 3 Candidates (NIST 仍在评估)
│   ├── 格: HAWK
│   ├── 多变量: MAYO, MQOM, QR-UOV, SNOVA, UOV
│   ├── 编码: SDitH
│   ├── 对称: FAEST
│   └── 同源: SQIsign
│
└── 🔬 China-Related Research (研究/国内候选)
    ├── KEM: CTRU, Aigis-enc, NEV, Scloud+, LAC
    └── 签名: Aigis-sig
```

---

## Common Selection Mistakes ⚠️

1. **"选签名最小的那个"** → 小签名可能意味着巨大的公钥（UOV: sig=96B 但 pk=66KB）或极复杂的实现（SQIsign）
2. **"ML-KEM 能加密文件"** → KEM 只建立共享密钥，加密需要 DEM（Data Encapsulation Mechanism）
3. **"候选和标准一样可靠"** → Round 3 候选可能在下一轮被修改或淘汰
4. **"一个算法就够了"** → 推荐 hybrid mode（传统+PQC），避免单点失败
5. **"所有场景用同一个安全级别"** → Level 1 对大多数场景足够，Level 5 用于长期机密或高安全需求
6. **"中国算法就是 SM 标准"** → 数据库中的中国算法是研究/候选/草案级别，除非有正式的 GM/T 标准文档

---

## Usage for the Agent

When a user asks "which algorithm should I use?":

1. First ask: KEM or Signature? (or both?)
2. Then ask: Must it be a final standard, or are future standards / candidates acceptable?
3. Then ask: What's the primary constraint? (bandwidth / speed / implementation simplicity / security conservatism)
4. Then use this guide to give a ranked recommendation with reasoning.
5. Always cite the relevant parameter table for exact sizes.
6. Always note the standardization status of every recommended algorithm.
