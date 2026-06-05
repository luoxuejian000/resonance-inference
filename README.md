# 🔮 Resonance Inference — 谐振推理引擎

> 基于晶脉哲学与谐振理论的新一代 AI 推理框架，让模型的思考过程在概念一致性与矛盾动力之间达成动态平衡。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![ThinkCheck](https://img.shields.io/badge/ThinkCheck-3.0-purple.svg)](https://github.com/luoxuejian000/-thinkcheck-lib-)

---

## ✨ 项目简介

**Resonance Inference** 是一个实验性的 AI 推理引擎，它将传统的“链式推理”重新定义为“谐振推理”——让模型的每一步思考，都如同一个自洽的共鸣腔，在统一性、发展性和对抗性之间寻找到最优的平衡点。

**它能做什么？**
- **谐振推理**：不是简单地生成下一个 Token，而是让每个推理步骤都经过 U/D/A/H 四维评估，确保逻辑自洽。
- **概念锚定**：通过“认知框架”指令，在长上下文中稳定维持模型的核心思维模式，防止语言或逻辑漂移。
- **矛盾捕获**：内置矛盾检测器，能在推理过程中实时发现并标记自相矛盾之处，并提供调谐建议。

---

## 🎯 项目定位

| 对比维度 | 传统推理 | 谐振推理 |
| :--- | :--- | :--- |
| **推理方式** | 线性 Token 生成 | 动态平衡的四维谐振 |
| **概念一致性** | 随上下文衰减 | 认知框架锚定，持久稳定 |
| **矛盾处理** | 被动忽略 | 主动检测、标记、调谐 |
| **理论根基** | 统计概率 | 晶脉哲学与谐振理论 |

---

## 🧠 理论背景

本项目基于**晶脉哲学**的四重公理与工程映射：

| 公理 | 核心命题 | 在推理中的工程映射 |
| :--- | :--- | :--- |
| **关系本体论** | 存在即关系，实在即关系网络 | **U (统一性)**：推理链中概念间的关系一致性 |
| **矛盾动力论** | 矛盾是系统演化的内在动力 | **D (发展性)**：推理的递进深度；**A (对抗性)**：自我质疑与反思 |
| **实践介入论** | 观察者本身改变被观察系统 | 认知框架指令对推理过程的结构性影响 |
| **谐振调谐论** | 最优状态是各维度间的动态平衡 | **H (和谐度)** = λU·U + λD·D - λA·A |

---

## 🏗️ 核心架构

```
用户输入 / Agent 任务
        │
        ▼
┌─────────────────────────────────────────┐
│         Resonance Inference Engine      │
│                                         │
│  ┌─────────────┐    ┌───────────────┐   │
│  │  Cognitive  │    │   Resonance   │   │
│  │   Frame     │───▶│    Evaluator  │   │
│  │  (认知框架)  │    │  (谐振评估器)  │   │
│  └─────────────┘    └───────────────┘   │
│                            │             │
│                            ▼             │
│  ┌─────────────────────────────────┐    │
│  │    Contradiction Detector       │    │
│  │       (矛盾检测器)               │    │
│  └─────────────────────────────────┘    │
│                            │             │
│                            ▼             │
│  ┌─────────────────────────────────┐    │
│  │    Harmonic Tuning Output       │    │
│  │       (谐振调谐输出)             │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 基础使用

```python
from resonance_inference import ResonanceInferenceEngine

# 初始化引擎
engine = ResonanceInferenceEngine(domain="general")

# 输入推理文本
reasoning_text = """
根据股权转让协议，我方已于去年完成全部出资义务，因此我方持有公司51%的股权。
所以，我方并未持有公司多数股权。
"""

# 执行谐振推理评估
report = engine.evaluate(reasoning_text)

print(f"和谐度 H: {report.H:.3f}")
print(f"统一性 U: {report.U:.3f}")
print(f"发展性 D: {report.D:.3f}")
print(f"对抗性 A: {report.A:.3f}")
print(f"病理判定: {report.pathology}")
```

### 3. 使用认知框架指令

```python
# 设置认知框架，增强推理稳定性
engine.set_cognitive_frame("用中文逻辑思维方式进行严谨推理")

# 在长上下文任务中使用
result = engine.infer(long_context_text)
```

---

## 📊 评估指标说明

| 指标 | 含义 | 理想范围 | 说明 |
| :--- | :--- | :--- | :--- |
| **U (统一性)** | 概念语义一致性 | 0.7 - 1.0 | 关键术语在推理链中是否保持含义稳定 |
| **D (发展性)** | 推理递进深度 | 0.3 - 0.8 | 推理是否有实质推进，而非原地打转 |
| **A (对抗性)** | 自我质疑与反思 | 0.0 - 0.3 | 适度反思有益，过高则自相矛盾 |
| **H (和谐度)** | 综合推理健康度 | 越高越好 | H = λU·U + λD·D - λA·A |

---

## 📁 项目结构

```
resonance-inference/
├── resonance_inference/          # 核心模块
│   ├── __init__.py
│   ├── engine.py                 # 推理引擎主类
│   ├── evaluator.py              # 四维评估器
│   ├── cognitive_frame.py        # 认知框架管理
│   └── contradiction_detector.py # 矛盾检测器
├── examples/
│   └── basic_usage.py            # 基础使用示例
├── tests/
│   └── test_engine.py            # 引擎测试
├── docs/
│   └── theory.md                 # 理论详解
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🔗 相关项目

| 项目 | 说明 | 链接 |
| :--- | :--- | :--- |
| **ThinkCheck 3.0 SDK** | 通用谐振评估引擎 | [查看](https://github.com/luoxuejian000/-thinkcheck-lib-/tree/3.0-harmony-sdk) |
| **水晶之心** | Hermes Agent × ThinkCheck 集成版 | [查看](https://github.com/luoxuejian000/hermes-agent) |
| **紫天鹅** | OpenClaw × ThinkCheck MCP 服务 | [查看](https://github.com/luoxuejian000/-Purple-Suan-) |
| **OCHR 集群框架** | 多节点 AI Agent 集群治理 | [查看](https://github.com/luoxuejian000/OCHR) |
| **ThinkCheck Agent** | 企业级文档智能调谐系统 | [查看](https://github.com/luoxuejian000/-thinkcheck-lib-/tree/thinkcheck-agent-v6) |

---

## 📄 开源许可

本项目遵循 [MIT License](LICENSE)。核心理论基于李广好独创的**晶脉哲学与谐振理论**。

---

**🔮 Resonance Inference — 让 AI 的每一步思考，都在谐振中找到自己的频率。**
```
