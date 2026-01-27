# Claude API Cost Optimization

> 💰 Save 50-90% on Claude API costs with three officially verified techniques

## Trigger

`/api-cost` or automatically when discussing Claude API usage, pricing, or optimization

---

## Quick Reference

| Technique | Savings | Use When |
|-----------|---------|----------|
| **Batch API** | 50% | Tasks can wait up to 24h |
| **Prompt Caching** | 90% | Repeated system prompts (>1K tokens) |
| **Extended Thinking** | ~80% | Complex reasoning tasks |
| **Batch + Cache** | ~95% | Bulk tasks with shared context |

---

## 1. Batch API (50% Off)

### When to Use
- ✅ Bulk translations
- ✅ Daily content generation
- ✅ Overnight report processing
- ❌ Real-time chat
- ❌ Immediate responses needed

### Code Example
```python
import anthropic

client = anthropic.Anthropic()

batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": "task-001",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Task 1"}]
            }
        },
        {
            "custom_id": "task-002",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Task 2"}]
            }
        }
    ]
)

# Wait for completion (up to 24h, usually <1h)
# Then retrieve results
for result in client.messages.batches.results(batch.id):
    print(f"{result.custom_id}: {result.result.message.content[0].text}")
```

### Limits
- Max 100,000 requests or 256MB per batch
- Results available for 29 days
- Most complete within 1 hour

---

## 2. Prompt Caching (90% Off)

### When to Use
- ✅ Long system prompts (>1K tokens)
- ✅ Repeated instructions
- ✅ RAG with large context
- ❌ Prompts < 1,024 tokens (won't cache)
- ❌ Frequently changing prompts

### Code Example
```python
import anthropic

client = anthropic.Anthropic()

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

# First call: Cache write (+25% cost)
# Subsequent calls: Cache read (-90% cost!)
```

### Pricing
| Type | Sonnet Price | vs Normal |
|------|--------------|-----------|
| Normal | $3/MTok | Baseline |
| Cache write | $3.75/MTok | +25% (first time) |
| Cache read | $0.30/MTok | **-90%** |

### Cache Rules
- Minimum: 1,024 tokens (Sonnet), 4,096 tokens (Opus/Haiku 4.5)
- TTL: 5 minutes (refreshes on use), or 1 hour (extra cost)
- Invalidation: Any change to cached content

---

## 3. Extended Thinking (~80% Off)

### When to Use
- ✅ Complex code architecture
- ✅ Strategic planning
- ✅ Mathematical reasoning
- ✅ Debugging complex issues
- ❌ Simple Q&A
- ❌ Translations

### Code Example
```python
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # Thinking budget
    },
    messages=[{
        "role": "user",
        "content": "Design an optimal architecture for..."
    }]
)

for block in response.content:
    if block.type == "thinking":
        print("🧠 Thinking:", block.thinking)
    elif block.type == "text":
        print("📝 Answer:", block.text)
```

### Pricing
- Input: $3/MTok
- Thinking output: ~$3/MTok (cheaper!)
- Final output: $15/MTok

---

## Combining Techniques

### Batch + Cache (Maximum Savings)
```python
# For batch requests with shared context
batch = client.messages.batches.create(
    requests=[
        {
            "custom_id": f"task-{i}",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "system": [{
                    "type": "text",
                    "text": "Shared system prompt...",
                    "cache_control": {"type": "ephemeral", "ttl": "1h"}
                }],
                "messages": [{"role": "user", "content": f"Task {i}"}]
            }
        }
        for i in range(100)
    ]
)
```

**Tip**: Use 1-hour cache for batches (they may take >5 minutes)

---

## Cost Calculator

### Example: Daily Video Scripts

| Item | Tokens | Price | Cost |
|------|--------|-------|------|
| System prompt (cached) | 2,000 | $0.30/MTok | $0.0006 |
| User input × 30 | 15,000 | $1.50/MTok (batch) | $0.0225 |
| Output × 30 | 30,000 | $7.50/MTok (batch) | $0.225 |
| **Daily total** | | | **$0.25** |
| Without optimization | | | $1.50 |
| **Savings** | | | **83%** |

---

## Decision Flowchart

```
Is it urgent?
├── Yes → Use normal API
└── No → Can wait 24h?
    ├── Yes → Use Batch API (50% off)
    └── No → Continue below

Do you have repeated system prompts?
├── Yes (>1K tokens) → Use Prompt Caching (90% off)
└── No → Continue below

Is it complex reasoning?
├── Yes → Use Extended Thinking
└── No → Use normal API
```

---

## Common Mistakes

| Mistake | Solution |
|---------|----------|
| Caching <1K tokens | Won't cache; add more context |
| 5min cache expiring | Use 1h TTL or keep requests flowing |
| Changing cached content | Keep static content separate |
| Expecting instant batch | Allow up to 24h for completion |

---

## Official Docs

- [Prompt Caching](https://platform.claude.com/docs/en/docs/build-with-claude/prompt-caching)
- [Batch Processing](https://platform.claude.com/docs/en/docs/build-with-claude/batch-processing)
- [Extended Thinking](https://platform.claude.com/docs/en/docs/build-with-claude/extended-thinking)

---

*Last updated: 2026-01-28 | Verified against official Anthropic documentation*
