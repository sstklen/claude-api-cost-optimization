# 📊 Real Batch API Results

> Actual API usage data from Washin Village's content generation system

## Source File

```
msgbatch_01P9cfexHjDVqp6asaawozzh_results.jsonl
```

## Usage Summary

| Metric | Value |
|--------|-------|
| **Total Requests** | 3 |
| **Input Tokens** | 3,612 |
| **Output Tokens** | 6,016 |
| **Cache Creation** | 1,782 tokens (first request) |
| **Cache Read** | 3,564 tokens (subsequent requests) |
| **Service Tier** | `batch` ✅ |

## Cost Calculation

### Without Optimization

```
Input:  (3,612 + 1,782 + 3,564) × $3.00/MTok  = $0.0269
Output: 6,016 × $15.00/MTok                   = $0.0902
─────────────────────────────────────────────────────
Total:                                         $0.1171
```

### With Batch API + Prompt Caching

```
Input (batch):      3,612 × $1.50/MTok  = $0.0054
Cache write:        1,782 × $3.75/MTok  = $0.0067
Cache read:         3,564 × $0.30/MTok  = $0.0011
Output (batch):     6,016 × $7.50/MTok  = $0.0451
─────────────────────────────────────────────────────
Total:                                   $0.0583
```

### Savings

```
╔═══════════════════════════════════════════╗
║  Without optimization:  $0.1171           ║
║  With Batch + Cache:    $0.0583           ║
║  ─────────────────────────────────────    ║
║  💰 Saved: $0.0588 (50.2%)                ║
╚═══════════════════════════════════════════╝
```

## Projection at Scale

| Requests | Without Opt | With Opt | Savings |
|----------|-------------|----------|---------|
| 100 | $3.90 | $1.94 | $1.96 |
| 1,000 | $39.03 | $19.43 | $19.60 |
| 10,000 | $390.30 | $194.30 | **$196.00** |

## Evidence

### Request #1 (Cache Write)
```json
{
  "input_tokens": 1204,
  "cache_creation_input_tokens": 1782,
  "cache_read_input_tokens": 0,
  "output_tokens": 1986,
  "service_tier": "batch"
}
```

### Request #2 (Cache Hit!)
```json
{
  "input_tokens": 1204,
  "cache_creation_input_tokens": 0,
  "cache_read_input_tokens": 1782,  // ← 90% off!
  "output_tokens": 2016,
  "service_tier": "batch"
}
```

### Request #3 (Cache Hit!)
```json
{
  "input_tokens": 1204,
  "cache_creation_input_tokens": 0,
  "cache_read_input_tokens": 1782,  // ← 90% off!
  "output_tokens": 2014,
  "service_tier": "batch"
}
```

---

## Key Observations

1. **Cache Hit Rate: 66%** (2 out of 3 requests used cached prompt)
2. **Batch API confirmed** via `service_tier: "batch"`
3. **Combined savings: ~50%** from both techniques

---

*Data collected: January 2026*
*System: Washin Village Content Generation*
