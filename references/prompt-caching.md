# Prompt Caching Quick Reference

> 90% off for repeated system prompts

## When to Use

✅ **Good for:**
- Long system prompts (>1K tokens)
- Repeated instructions
- RAG with large context
- Multi-turn conversations

❌ **Not for:**
- Prompts < 1,024 tokens
- Frequently changing prompts
- One-off requests

## Pricing

| Type | Sonnet Price | vs Normal |
|------|--------------|-----------|
| Normal input | $3/MTok | Baseline |
| Cache write | $3.75/MTok | +25% (first time) |
| **Cache read** | **$0.30/MTok** | **-90%** |

## Minimum Token Requirements

| Model | Minimum Tokens |
|-------|----------------|
| Sonnet | 1,024 |
| Opus | 4,096 |
| Haiku 4.5 | 4,096 |

## Cache TTL (Time-To-Live)

| Type | Duration | Extra Cost |
|------|----------|------------|
| Ephemeral | 5 minutes | None |
| Extended | 1 hour | Small fee |

**Note:** Cache refreshes on each use. If you call every 4 minutes, it stays alive indefinitely.

## Basic Usage

```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "Your long system prompt here (must be >1024 tokens)...",
            "cache_control": {"type": "ephemeral"}  # ← Enable caching!
        }
    ],
    messages=[{"role": "user", "content": "User question"}]
)
```

## Cache Behavior

```
Request 1: Cache MISS → Write cache (+25%)
Request 2: Cache HIT  → Read cache (-90%) ✅
Request 3: Cache HIT  → Read cache (-90%) ✅
...
Request N: Cache HIT  → Read cache (-90%) ✅
```

## Important Notes

1. **Order matters** - Cached content must be at the beginning
2. **Exact match** - Any change invalidates the cache
3. **Images can't be cached** - Only text content
4. **Multi-turn caching** - Use `cache_control` on conversation history

---

*Source: [Anthropic Prompt Caching Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)*
