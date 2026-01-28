# 💰 Claude API Cost Optimization Skill

[![GitHub stars](https://img.shields.io/github/stars/sstklen/claude-api-cost-optimization?style=social)](https://github.com/sstklen/claude-api-cost-optimization)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

> **Save 50-90% on Claude API costs** with three officially verified techniques

## ⚡ Quick Start

```bash
# Install the skill
cp claude-api-cost-optimization.skill.md ~/.claude/skills/

# Calculate your potential savings
python scripts/calculate_savings.py --input 10000 --output 5000 --requests 100
```

## 💰 Three Techniques, Massive Savings

| Technique | Savings | Best For | Docs |
|-----------|---------|----------|------|
| **Batch API** | 50% off | Non-urgent bulk tasks | [Reference](references/batch-api.md) |
| **Prompt Caching** | 90% off | Repeated system prompts | [Reference](references/prompt-caching.md) |
| **Extended Thinking** | ~80% off | Complex reasoning | [Reference](references/extended-thinking.md) |

## 📊 Proof: Real Billing Data

### Latest: 294 Video Batch Job (2026-01-28)

| Item | Value |
|------|-------|
| Files Processed | 294 |
| Original Cost | $11.17 |
| **Batch Cost** | **$5.59** |
| **💰 Savings** | **$5.59 (50%)** |

👉 **Full case study:** [examples/batch-294-videos-case-study.md](examples/batch-294-videos-case-study.md)

### Anthropic Console CSV Export (2026-01-27)

| Usage Type | Input Tokens | Cache Read | Output | Savings Applied |
|------------|--------------|------------|--------|-----------------|
| Sonnet (standard) | 79,224 | **39,204** ✅ | 71,608 | Caching working! |
| Sonnet (batch) | 3,612 | **3,564** ✅ | 6,016 | Batch + Cache! |

👉 **Full analysis:** [examples/billing-data-analysis.md](examples/billing-data-analysis.md)

### Real-World Results (294 Videos)

| Optimization | Cost/Video | Total | Savings |
|--------------|------------|-------|---------|
| None | $0.038 | $11.14 | — |
| + Caching | $0.033 | $9.62 | 14% |
| + Batch | $0.019 | $5.57 | 50% |
| **+ Both** | **$0.016** | **$4.79** | **57%** 🔥 |

👉 **Full report:** [examples/GAIA-savings-report.md](examples/GAIA-savings-report.md)

## 🔧 Code Examples

### Prompt Caching (90% off repeated prompts)

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    system=[{
        "type": "text",
        "text": "Your long system prompt (>1024 tokens)...",
        "cache_control": {"type": "ephemeral"}  # ← This saves 90%!
    }],
    messages=[{"role": "user", "content": "Hello"}]
)
```

### Batch API (50% off everything)

```python
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "task-001",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Translate..."}]
            }
        }
        # Add up to 100,000 requests!
    ]
)
```

👉 **Full scripts:** [scripts/](scripts/)

## 💡 Key Insight: Image Workloads

> **Why only 14% caching savings instead of 90%?**

In image tasks, images = ~85% of tokens. Only the system prompt (~15%) is cacheable.

```
Input Composition:
├── System Prompt: ~15% → ✅ Cacheable (90% off)
└── Image Data:    ~85% → ❌ Cannot cache

Actual Savings: 15% × 90% = ~14%
```

**This is NOT in the official docs — we learned it the hard way!**

---

## 📁 Repository Structure

```
├── claude-api-cost-optimization.skill.md  # ← Install this!
│
├── examples/                    # Real evidence
│   ├── billing-data-analysis.md # Anthropic Console CSV
│   ├── real-batch-results.md    # Actual API response
│   └── GAIA-savings-report.md   # 294 video case study
│
├── scripts/                     # Ready-to-run code
│   ├── batch_example.py
│   ├── cache_example.py
│   └── calculate_savings.py
│
└── references/                  # Quick cheatsheets
    ├── batch-api.md
    ├── prompt-caching.md
    └── extended-thinking.md
```

## 📊 Pricing Reference (2026)

| Model | Input | Output | Batch Input | Batch Output |
|-------|-------|--------|-------------|--------------|
| Opus 4.5 | $5/MTok | $25/MTok | $2.50/MTok | $12.50/MTok |
| Sonnet 4.5 | $3/MTok | $15/MTok | $1.50/MTok | $7.50/MTok |
| Haiku 4.5 | $1/MTok | $5/MTok | $0.50/MTok | $2.50/MTok |

| Cache Type | Price | vs Normal |
|------------|-------|-----------|
| Cache write | $3.75/MTok | +25% (first time) |
| **Cache read** | **$0.30/MTok** | **-90%** ✅ |

## 🔗 Official Docs

- [Prompt Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Batch Processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)
- [Extended Thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)

---

## 🐾 The Story (Optional Reading)

This skill was born from **[Washin Village](https://washinmura.jp)** — home of 28 cats & dogs in Japan. While building our AI pet recognition system, API bills added up quickly. We researched every cost-saving technique and compiled them here.

> Full story: [STORY.md](STORY.md)

---

*Made with 💰 by Washin Village — Save money, make more content!*
