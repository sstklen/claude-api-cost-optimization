# Batch API Quick Reference

> 50% off all API costs for non-urgent tasks

## When to Use

✅ **Good for:**
- Bulk translations
- Daily content generation
- Overnight report processing
- Large-scale data analysis

❌ **Not for:**
- Real-time chat
- Immediate responses
- Interactive applications

## Pricing (50% Off)

| Model | Normal Input | Batch Input | Normal Output | Batch Output |
|-------|--------------|-------------|---------------|--------------|
| Opus | $5/MTok | $2.50/MTok | $25/MTok | $12.50/MTok |
| Sonnet | $3/MTok | $1.50/MTok | $15/MTok | $7.50/MTok |
| Haiku | $1/MTok | $0.50/MTok | $5/MTok | $2.50/MTok |

## Limits

- Max requests per batch: **100,000**
- Max batch size: **256 MB**
- Processing time: Up to **24 hours** (usually < 1 hour)
- Results available: **29 days**

## Basic Usage

```python
import anthropic
client = anthropic.Anthropic()

# Create batch
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "task-001",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hello"}]
            }
        }
    ]
)

# Check status
batch = client.messages.batches.retrieve(batch.id)
print(batch.processing_status)  # "in_progress" or "ended"

# Get results
for result in client.messages.batches.results(batch.id):
    print(f"{result.custom_id}: {result.result.message.content[0].text}")
```

## Status Values

| Status | Meaning |
|--------|---------|
| `in_progress` | Still processing |
| `ended` | Complete (check request_counts) |
| `canceling` | Cancel requested |
| `canceled` | Successfully canceled |

---

*Source: [Anthropic Batch Processing Docs](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)*
