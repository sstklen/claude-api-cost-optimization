# 💰 Claude API Cost Optimization Skill

[![GitHub stars](https://img.shields.io/github/stars/sstklen/claude-api-cost-optimization?style=social)](https://github.com/sstklen/claude-api-cost-optimization)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> 💰 Save 50-90% on Claude API costs with three officially verified techniques


![Claude API Cost Optimization Preview](assets/preview.png)

[English](#english) | [日本語](#日本語) | [中文](#中文) | [📖 背景故事 / Story](STORY.md)

---

## 🐾 The Story

This skill was born from **[Washin Village](https://github.com/sstklen)** — home of 28 cats & dogs in Japan.

While building our AI pet recognition system, we ran many agents using **[infinite-gratitude](https://github.com/sstklen/infinite-gratitude)** (our multi-agent research skill). The API bills added up quickly, so we researched every cost-saving technique and compiled them here.

**From one cat's "gift" came two open-source skills!** 🐱

> Read the full story: [STORY.md](STORY.md)

---

<a name="english"></a>
## 🇺🇸 English

### The Problem

Claude API costs can add up quickly:
- Sonnet: $3 input / $15 output per million tokens
- Opus: $15 input / $75 output per million tokens

### The Solution

Three officially verified techniques that can save you **50-90%**:

| Technique | Savings | Best For |
|-----------|---------|----------|
| **Batch API** | 50% off | Non-urgent bulk tasks |
| **Prompt Caching** | 90% off | Repeated system prompts |
| **Extended Thinking** | ~80% off | Complex reasoning (thinking portion) |

### Quick Example

```python
# ❌ Without optimization: $3/MTok
response = client.messages.create(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": "Hello"}]
)

# ✅ With Prompt Caching: $0.30/MTok (90% savings!)
response = client.messages.create(
    model="claude-sonnet-4-5",
    system=[{
        "type": "text",
        "text": "Your long system prompt here...",
        "cache_control": {"type": "ephemeral"}  # ← Magic line!
    }],
    messages=[{"role": "user", "content": "Hello"}]
)
```

### 🎯 Real World Case Study: GAIA v4.8.2

We battle-tested all techniques in **GAIA** (Global AI Intelligence for Animals) — our animal recognition system processing 294 videos.

#### Results

| Technique | Expected Savings | Actual Savings | Status |
|-----------|-----------------|----------------|--------|
| Prompt Caching | -90% | **-14%** | ✅ Working |
| Batch API | -50% | **-50%** | ✅ Working |
| Cache + Batch | -95% | **-57%** | ✅ Working |

#### Cost Breakdown (294 videos)

| Mode | Per Video | Total | Savings |
|------|-----------|-------|---------|
| Original | $0.038 | $11.14 | — |
| + Caching | $0.033 | $9.62 | 14% |
| + Batch | $0.019 | $5.57 | 50% |
| **+ Both** | **$0.016** | **$4.79** | **57%** 🔥 |

#### 💡 Key Insight: Image-Heavy Workloads

> **Why only 14% savings from caching instead of 90%?**
>
> In image recognition tasks, **images account for ~85% of input tokens**.
> Only the system prompt (~15%) can be cached.
>
> ```
> Input Composition:
> ├── System Prompt: ~15% → ✅ Cacheable (saves 90%)
> └── Image Data:    ~85% → ❌ Cannot cache
>
> Overall Savings: 15% × 90% = ~14%
> ```

This is **not documented** in the official Anthropic docs — we learned it the hard way!

### Installation

```bash
# Copy to your Claude Code skills folder
cp claude-api-cost-optimization.skill.md ~/.claude/skills/
```

### Real Results

| Scenario | Before | After | Savings |
|----------|--------|-------|---------|
| 30 daily video scripts | $1.50/day | $0.27/day | **82%** |
| AI Director prompts | $0.90/day | $0.10/day | **89%** |
| Batch translations | $3.00 | $1.50 | **50%** |

---

<a name="日本語"></a>
## 🇯🇵 日本語

### 問題

Claude APIのコストは高くなりがちです：
- Sonnet: 入力$3 / 出力$15（100万トークンあたり）
- Opus: 入力$15 / 出力$75（100万トークンあたり）

### 解決策

公式に検証された3つのテクニックで**50-90%節約**：

| テクニック | 節約率 | 最適な用途 |
|-----------|--------|----------|
| **Batch API** | 50%オフ | 急がない一括タスク |
| **Prompt Caching** | 90%オフ | 繰り返しのシステムプロンプト |
| **Extended Thinking** | 約80%オフ | 複雑な推論（思考部分）|

### インストール

```bash
# Claude Codeのskillsフォルダにコピー
cp claude-api-cost-optimization.skill.md ~/.claude/skills/
```

---

<a name="中文"></a>
## 🇹🇼 中文

### 問題

Claude API 費用很容易累積：
- Sonnet: 輸入 $3 / 輸出 $15（每百萬 token）
- Opus: 輸入 $15 / 輸出 $75（每百萬 token）

### 解決方案

三個官方驗證的技巧，可省 **50-90%**：

| 技巧 | 節省 | 適用場景 |
|------|------|---------|
| **Batch API** | 50% off | 不急的批量任務 |
| **Prompt Caching** | 90% off | 重複的系統提示 |
| **Extended Thinking** | ~80% off | 複雜推理（思考部分）|

### 安裝

```bash
# 複製到 Claude Code skills 資料夾
cp claude-api-cost-optimization.skill.md ~/.claude/skills/
```

---

## 📊 Pricing Reference (2026)

| Model | Input | Output | Batch Input | Batch Output |
|-------|-------|--------|-------------|--------------|
| Opus 4.5 | $5/MTok | $25/MTok | $2.50/MTok | $12.50/MTok |
| Sonnet 4.5 | $3/MTok | $15/MTok | $1.50/MTok | $7.50/MTok |
| Haiku 4.5 | $1/MTok | $5/MTok | $0.50/MTok | $2.50/MTok |

### Prompt Caching Pricing

| Type | Sonnet Price | vs Normal |
|------|--------------|-----------|
| Normal input | $3/MTok | Baseline |
| Cache write (5min) | $3.75/MTok | +25% |
| **Cache read** | **$0.30/MTok** | **-90%** |

---

## 📁 Files

```
├── README.md                              # This file
├── STORY.md                               # The backstory
├── assets/preview.png                     # Preview image
└── claude-api-cost-optimization.skill.md  # The skill (copy this!)
```

---

## 🔗 Official Documentation

- [Prompt Caching](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching)
- [Batch Processing](https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing)
- [Extended Thinking](https://platform.claude.com/docs/en/docs/build-with-claude/extended-thinking)
- [Pricing](https://claude.com/pricing)

---

## 🐾 Credits

Made with 💰 by [Washin Village](https://washinmura.jp) — Home of 28 cats & dogs in Japan's Boso Peninsula.

*Save money, make more content!*
