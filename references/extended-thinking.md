# Extended Thinking Quick Reference

> Better reasoning at lower cost per insight

## When to Use

✅ **Good for:**
- Complex code architecture
- Strategic planning
- Mathematical reasoning
- Debugging difficult issues
- Multi-step analysis

❌ **Not for:**
- Simple Q&A
- Translations
- Data extraction
- Quick lookups

## Pricing

| Type | Price |
|------|-------|
| Input tokens | $3/MTok |
| Thinking tokens | ~$3/MTok (cheaper than output!) |
| Output tokens | $15/MTok |

**Key insight:** Thinking tokens are priced like input, not output. Complex reasoning in the thinking phase costs 5x less than in the output!

## Basic Usage

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

# Access thinking and response
for block in response.content:
    if block.type == "thinking":
        print("🧠 Thinking:", block.thinking)
    elif block.type == "text":
        print("📝 Answer:", block.text)
```

## Budget Tokens

| Budget | Best For |
|--------|----------|
| 5,000 | Moderate complexity |
| 10,000 | Complex analysis |
| 20,000 | Very difficult problems |
| 50,000+ | Research-level reasoning |

## Cost Comparison Example

**Task:** Design a microservices architecture

| Approach | Tokens | Cost |
|----------|--------|------|
| Normal (all output) | 5,000 output | $0.075 |
| Extended thinking | 4,000 thinking + 1,000 output | $0.027 |
| **Savings** | | **64%** |

## Tips

1. **Set appropriate budget** - Don't over-allocate
2. **Use for reasoning** - Not simple tasks
3. **Combine with caching** - Cache the system prompt
4. **Review thinking** - Learn from Claude's reasoning process

---

*Source: [Anthropic Extended Thinking Docs](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)*
