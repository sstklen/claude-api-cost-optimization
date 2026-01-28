# 📊 Case Study: 294 Video Batch Processing

> Real Batch API submission with actual cost savings

## Job Details

| Item | Value |
|------|-------|
| **Batch ID** | `msgbatch_01KuerZBFziJmiaBm7Sv6axB` |
| **Files Processed** | 294 |
| **Original Cost** | $11.17 |
| **Batch Cost** | $5.59 |
| **💰 Savings** | **$5.59 (50%)** |
| **Expected Wait** | 1-24 hours (usually <1 hour) |

## Time Breakdown

| Stage | Description | Time |
|-------|-------------|------|
| **Packaging** | Scan 294 JSONs + Extract keyframes + Convert to Base64 | ~30 sec |
| **Submit** | Upload to Anthropic API | ~1 sec |
| **Processing** | Claude Sonnet batch analysis (Anthropic side) | Usually <1 hour |
| **Retrieve** | Download results + Update JSONs | ~5 min |

## Speed vs Cost Comparison

| Mode | Time | Cost | Cost/File |
|------|------|------|-----------|
| Real-time | ~15 min (294 × 3sec) | $11.17 | $0.038 |
| **Batch** | <1.5 hours | **$5.59** | **$0.019** |

## Visual Summary

```
┌─────────────────────────────────────────────────────────┐
│                    294 Videos                           │
├─────────────────────────────────────────────────────────┤
│  Real-time Mode                                         │
│  ████████████████████████████████████████ $11.17       │
│                                                         │
│  Batch Mode                                             │
│  ████████████████████ $5.59                            │
│                       ↑                                 │
│                    50% OFF                              │
└─────────────────────────────────────────────────────────┘
```

## When to Use Batch API

✅ **Good for this use case:**
- Video analysis (not time-sensitive)
- Bulk content tagging
- Overnight processing jobs
- Any task where you can wait 1-24 hours

❌ **Don't use for:**
- Real-time chat
- Interactive applications
- Urgent responses needed

## Key Insight

> **50% savings is GUARANTEED** — Batch API always costs half of real-time API.
>
> The only trade-off is time: you wait up to 24 hours (usually <1 hour).
>
> For batch jobs like this, it's a no-brainer!

---

*Data source: Actual Batch API submission*
*Date: 2026-01-28*
*System: GAIA Video Analysis Pipeline*
