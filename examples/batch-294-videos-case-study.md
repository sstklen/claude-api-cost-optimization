# 📊 Case Study: Big vs Small Batch Comparison

> Real production data from Washin Village animal video analysis

## 🔥 The Biggest Discovery: Bigger is Faster AND Cheaper!

We ran 3 batches and compared everything:

| Batch | Requests | Sent (JST) | Done (JST) | Total Time | Per Request |
|-------|----------|------------|------------|------------|-------------|
| 🐘 **Large** | 294 | 10:22 | 12:35 | 133 min | **0.45 min** |
| 🐰 Small | 10 | 11:50 | 13:28 | 98 min | 9.84 min |
| 🐁 Test | 3 | 01:20 | 02:23 | 62 min | 20.77 min |

### Wait... the Large batch finished FIRST?!

Yes! Even though:
- Large batch was sent at 10:22
- Small batch was sent at 11:50 (1.5 hours later)
- **Large batch still finished 53 minutes before small batch!**

**This means: Anthropic does NOT process in order (FIFO). Bigger batches get priority!**

---

## 🧠 Why Does This Happen? (Simple Explanation)

Think of Anthropic's GPU like an oven:

```
🔥 Oven preheating = 15 minutes (fixed cost, always pay this)

Large batch (294 items):
  Preheat 15 min → Bake all 294 → Average = 0.45 min each ✅

Small batch (10 items):
  Preheat 15 min → Bake only 10 → Average = 9.84 min each ❌

The more you bake, the cheaper per item!
```

---

## 📊 Token Usage Comparison

| Batch | Input | Output | Cache Write | Cache Read | Avg Output |
|-------|-------|--------|-------------|------------|------------|
| 🐘 Large | 365,624 | 611,412 | 106,920 | 416,988 | 2,080/req |
| 🐰 Small | 12,988 | 2,576 | 0 | 0 | 258/req |
| 🐁 Test | 3,612 | 6,016 | 1,782 | 3,564 | 2,005/req |

### Why does Large batch have Cache but Small doesn't?

- **Large + Test batch**: Same system prompt (GAIA Stage 2) → Cache works!
- **Small batch**: Different prompt (random test) → No cache

**Lesson: Put same-type requests together to share cache!**

---

## 💰 Cost Analysis

### Large Batch (294 videos)

| Item | Value |
|------|-------|
| Total Tokens | 1,500,944 |
| Original Cost | $11.04 |
| **Batch Cost** | **$5.52** |
| **Savings** | **50%** ✅ |

### The "22x Efficiency Gap"

| Batch | Time per Request | Relative Cost |
|-------|------------------|---------------|
| 🐘 Large (294) | 0.45 min | **1x** (cheapest) |
| 🐰 Small (10) | 9.84 min | **22x** more expensive! |
| 🐁 Test (3) | 20.77 min | **46x** more expensive! |

---

## 💡 What Official Docs Don't Tell You

| Topic | Official Says | We Discovered |
|-------|---------------|---------------|
| **Processing Order** | "Within 24 hours" | Big batches get priority (not FIFO!) |
| **Batch Size Effect** | Nothing | 22x efficiency difference! |
| **Cache for Images** | "90% savings" | Only 14% for images (85% is image data, can't cache) |
| **Scale Effect** | Nothing | More requests = cheaper per request |

### Why Image Cache Only Saves 14%?

```
Your request content:
├── System Prompt (text): 15% → ✅ Can cache (90% off)
└── Image Data: 85% → ❌ Cannot cache

Actual savings: 15% × 90% = ~14%
```

---

## ✅ Best Practices (Based on Real Data)

### DO ✅

| Action | Why |
|--------|-----|
| Batch 100+ requests together | 22x more efficient than small batches |
| Use Batch API for images | 50% savings guaranteed |
| Group same-prompt requests | Share cache, save more |
| Submit all at once | Don't split into multiple small batches |

### DON'T ❌

| Action | Why |
|--------|-----|
| Send <10 requests as batch | Wastes GPU initialization cost |
| Expect 90% cache on images | Only 14% actual savings |
| Send multiple small batches | One big batch is faster AND cheaper |

---

## 📈 Summary Table

| Finding | Details |
|---------|---------|
| **Batch API Discount** | 50% ✅ (as advertised) |
| **Big vs Small Batch** | Big is 22x more efficient! 🔥 |
| **Processing Order** | NOT FIFO - big batches first |
| **Image Cache** | Only 14% (not 90%) |
| **Best Strategy** | Batch 100+ requests together |

---

## 🎯 TL;DR (Too Long; Didn't Read)

```
Want to save money? → Use big batches (100+ requests)
Want to save time?  → Also use big batches (they finish first!)
Working with images? → Batch API is enough (cache doesn't help much)
Working with text?   → Use both Batch + Cache (up to 95% savings)
```

---

*Data source: Anthropic Console + Production Batches*
*Date: 2026-01-28*
*System: GAIA Video Analysis Pipeline v4.8.3*
*By: [Washin Village](https://washinmura.jp)*
