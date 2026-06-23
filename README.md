# PQC Quickstart Tutor — 后量子密码快速入门讲师

[English](#pqc-quickstart-tutor) | [中文](#后量子密码快速入门讲师)

---

# PQC Quickstart Tutor

A teaching-oriented post-quantum cryptography agent for engineers and researchers. **Download. Open. Ask.** No API keys, no servers, no dependencies.

## 🚀 Quick Start (5 seconds)

```bash
# Step 1: Open in your AI tool
cd PQC_Agent
claude            # or: codex ., cursor ., windsurf ., code .

# Step 2: Just ask — the agent auto-activates
"Explain ML-KEM like you would ECDH"
"Compare Falcon vs ML-DSA key sizes"
"Which PQC signature should I use for IoT?"
```

That's it. The agent loads `CLAUDE.md` automatically. All answers are sourced from the verified database.

### Or use the one-click launcher

```bash
./install.bat          # One-time setup (adds to PATH, creates shortcuts)
pqc-tutor              # Launch from anywhere
pqc-tutor "query"      # One-shot question from anywhere
```

### In other AI tools, same experience:

| You type... | In this tool... | What happens |
|---|---|---|
| `@PQC_AGENT explain Falcon` | Cursor | Opens agent context from `.cursor/rules/` |
| `/pqc` | Claude Code | Activates PQC Tutor slash command |
| `@workspace what is ML-KEM` | GitHub Copilot | Uses `.github/copilot-instructions.md` |
| Just ask a PQC question | Any tool in this folder | Agent auto-detects and activates |

Full setup guide: **[PLATFORMS.md](PLATFORMS.md)**

## 🎓 Live Demos

See the agent in action with real, database-sourced answers:

| Demo | What it shows |
|---|---|
| **[Explaining ML-KEM](docs/demo_mlkem.md)** | Full teaching flow: ECDH analogy → KEM API → NTT math → parameter tables → common misunderstandings |
| **[Choosing a Signature](docs/demo_signature_choice.md)** | Constraint-based selection: clarifying questions → head-to-head comparison → ranked recommendations → visual size charts |

## 📊 What's Inside

### Knowledge Base (38 Markdown files)
- **Parameter tables:** Every PQC algorithm's exact key/signature/ciphertext sizes (verified against source PDFs)
- **Algorithm cards:** 20+ one-page teaching cards (ML-KEM → SQIsign)
- **Guides:** Algorithm selection decision tree + panoramic cross-algorithm comparison
- **Benchmarks:** Hardware (Falcon FPGA + ASIC) + Software (HQC, Aigis, Scloud+)
- **Standard status:** Precise NIST/China standardization tracking
- **Anti-hallucination rules:** Guardrails to prevent fabricated numbers

### Primary Sources (35 PDFs)
- FIPS 203/204/205 (NIST PQC standards)
- Falcon, HQC specifications (selected future standards)
- 9 NIST Additional Signature Round 3 candidate specs
- 9 China-related papers/drafts (Aigis, CTRU, NEV, Scloud+, LAC)
- NIST migration reports, surveys

### Algorithm Coverage (25+ algorithms)

| Category | Algorithms |
|----------|-----------|
| ✅ FIPS Standards | ML-KEM, ML-DSA, SLH-DSA |
| 🔶 Future Standards | Falcon/FN-DSA, HQC |
| 🔷 Round 3 Candidates | FAEST, HAWK, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign, UOV |
| 🔬 China Research | Aigis-enc, Aigis-sig, Scloud+, CTRU/CNTR, NEV, LAC |

## 🎯 Who This Is For

- **Software engineers** integrating PQC into TLS/SSH/VPN
- **Hardware/FPGA engineers** evaluating PQC implementation cost
- **Security architects** planning PQC migration
- **Researchers** needing quick parameter lookups
- **Students** learning PQC from a conventional-crypto background

## 🛡️ Anti-Hallucination

The agent is built on a strict rule: **concepts may be explained freely, but numerical claims must be sourced from the database.** It will say "not available" rather than fabricate parameters, sizes, or benchmarks.

## 📁 Project Structure

```
PQC_Agent/
├── AGENTS.md                           ← Universal agent definition
├── CLAUDE.md                           ← Claude Code (extended)
├── PLATFORMS.md                        ← Multi-platform setup guide
├── CONTRIBUTING.md                     ← How to add PDFs, cards, benchmarks
├── LICENSE                             ← Apache 2.0
├── NOTICE.md                           ← Third-party content notices
├── README.md                           ← This file (中英双语 / EN+ZH)
├── .cursor/rules/pqc-tutor.mdc        ← Cursor rules
├── .github/copilot-instructions.md     ← GitHub Copilot
├── .github/workflows/check.yml         ← CI integrity check
├── tools/check_database.py             ← Database validator
├── database/
│   ├── index.json                      ← Machine-readable file index
│   ├── metadata/                       ← Parameter tables, status, benchmarks
│   ├── guides/                         ← Selection guide, comparison tables
│   ├── alg_cards/                      ← 20+ algorithm teaching cards
│   ├── lessons/                        ← Starter lessons
│   ├── mapping/                        ← Traditional-to-PQC mapping
│   └── implementation/                 ← Hardware module concepts
├── docs/                               ← Live demos
│   ├── demo_mlkem.md
│   └── demo_signature_choice.md
└── official/                           ← 35 PDF primary sources
    ├── 01_nist_standards/              ← FIPS 203, 204, 205
    ├── 02_nist_reports_migration/
    ├── 03_selected_future_standards/    ← Falcon, HQC specs
    ├── 04_nist_additional_signatures_round3/
    ├── 05_china_related/               ← Aigis, CTRU, NEV, Scloud+, LAC
    └── 06_general_surveys/
```

## 🔧 Using as a Library

The `database/` files are plain Markdown. You can:

- **Read them directly** — all tables in standard Markdown format
- **Use with any LLM** — copy the compact prompt from `AGENTS.md`
- **Integrate into docs** — embed algorithm cards in your own documentation
- **Extend with new PDFs** — see [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 Database Versions

| Version | What changed |
|---------|-------------|
| v1 | Initial metadata layer: ML-KEM, ML-DSA, SLH-DSA parameter tables, anti-hallucination rules |
| v2 | Added Falcon, HQC, Aigis, Scloud+, CTRU, NEV extended parameters + software benchmarks |
| v3 | Added 9 NIST Additional Signatures Round 3 candidate tables + algorithm cards |

## ✅ Verification Status

All parameter tables verified against source PDFs: **2026-06-23**

- ML-KEM, ML-DSA, SLH-DSA ✅
- Falcon, HQC ✅
- Aigis-enc, Aigis-sig ✅
- Scloud+ ✅
- CTRU/CNTR (paper) ✅
- CTRU Chinese draft ✅
- NEV ✅
- FAEST, HAWK, UOV, SQIsign, MAYO, SNOVA, SDitH, MQOM, QR-UOV ✅

## 🤝 Contributing

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for how to:
- Add new PDFs and extract parameters
- Create algorithm teaching cards
- Add benchmarks
- Update the selection guide

## 📄 License

Apache License 2.0. See [LICENSE](LICENSE) for details. Third-party content notices in [NOTICE.md](NOTICE.md).

---

# 后量子密码快速入门讲师

面向工程师和研究人员的后量子密码教学智能体。**下载。打开。提问。** 无需 API 密钥，无需服务器，无需依赖。

## 🚀 五秒上手

```bash
# 第1步：在 AI 工具中打开
cd PQC_Agent
claude            # 或：codex ., cursor ., windsurf ., code .

# 第2步：直接提问 — agent 自动激活
"像解释ECDH一样解释ML-KEM"
"对比Falcon和ML-DSA的密钥大小"
"物联网场景应该用哪种PQC签名？"
```

就是这么简单。Agent 会自动加载 `CLAUDE.md`。所有回答都基于已验证的数据库。

## 🎓 真实演示

看看 agent 如何利用数据库给出真实、有源的回答：

| 演示 | 展示内容 |
|---|---|
| **[解释 ML-KEM](docs/demo_mlkem.md)** | 完整教学流程：ECDH类比 → KEM API → NTT数学 → 参数表 → 常见误解纠正 |
| **[选择签名算法](docs/demo_signature_choice.md)** | 约束驱动选型：澄清问题 → 横向对比 → 分级推荐 → 可视化大小对比 |

## 📊 内容概览

### 知识库（38个Markdown文件）
- **参数表：** 每个PQC算法的精确密钥/签名/密文大小（对照源PDF验证）
- **算法卡片：** 20+ 页单页教学卡片（ML-KEM → SQIsign）
- **选型指南：** 算法选择决策树 + 全景横向对比
- **基准测试：** 硬件Benchmark（Falcon FPGA + ASIC）+ 软件Benchmark（HQC, Aigis, Scloud+）
- **标准化追踪：** 精确的NIST/中国标准化状态
- **防幻觉规则：** 防止捏造数字的防护栏

### 原始文献（35个PDF）
- FIPS 203/204/205（NIST PQC标准）
- Falcon, HQC规范（已入选未来标准）
- 9个NIST附加签名Round 3候选规范
- 9个中国相关论文/草案（Aigis, CTRU, NEV, Scloud+, LAC）
- NIST迁移报告、综述

## 🎯 适用人群

- **软件工程师** — 在TLS/SSH/VPN中集成PQC
- **硬件/FPGA工程师** — 评估PQC实现成本
- **安全架构师** — 规划PQC迁移
- **研究人员** — 快速查询参数
- **学生** — 从传统密码学背景入门PQC

## 🛡️ 防幻觉机制

Agent遵循严格规则：**概念可以自由讲解，但数字必须从数据库获取。** 宁肯说"暂无数据"，也绝不捏造参数、密钥大小或Benchmark数字。

## 🤝 贡献

详见 **[CONTRIBUTING.md](CONTRIBUTING.md)**：
- 如何添加新PDF并提取参数
- 如何创建算法教学卡片
- 如何添加Benchmark
- 如何更新选型指南

## 📄 许可证

Apache License 2.0。详见 [LICENSE](LICENSE)。第三方内容声明：[NOTICE.md](NOTICE.md)。
