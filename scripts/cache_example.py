#!/usr/bin/env python3
"""
Prompt Caching Example - Save up to 90% on repeated system prompts

This script demonstrates how to use Claude's Prompt Caching
for workloads with repeated system prompts.

Usage:
    python cache_example.py

Requirements:
    pip install anthropic
"""

import anthropic
from typing import List

# Initialize client
client = anthropic.Anthropic()

# Long system prompt (must be >1024 tokens for Sonnet)
# This gets cached and reused across multiple requests
SYSTEM_PROMPT = """You are an expert AI assistant specializing in code review and software development best practices.

## Your Expertise Areas:
1. Code Quality: Clean code principles, SOLID principles, DRY, KISS
2. Security: OWASP Top 10, input validation, authentication, authorization
3. Performance: Algorithm optimization, database queries, caching strategies
4. Architecture: Design patterns, microservices, monoliths, event-driven systems
5. Testing: Unit tests, integration tests, E2E tests, TDD, BDD

## Review Guidelines:
When reviewing code, you should:
- Identify potential bugs and logic errors
- Suggest performance improvements
- Point out security vulnerabilities
- Recommend better naming conventions
- Suggest refactoring opportunities
- Check for proper error handling
- Verify edge cases are handled
- Ensure code follows language-specific best practices

## Response Format:
Structure your reviews as follows:
1. **Summary**: Brief overview of the code's purpose
2. **Strengths**: What the code does well
3. **Issues**: Problems found (Critical/Major/Minor)
4. **Suggestions**: Specific improvements with code examples
5. **Security Notes**: Any security concerns
6. **Performance Notes**: Any performance considerations

## Code Examples Reference:
Here are examples of common patterns you should recommend:

### Python - Error Handling
```python
# Bad
def get_user(id):
    return db.query(f"SELECT * FROM users WHERE id = {id}")

# Good
def get_user(id: int) -> Optional[User]:
    try:
        return db.query(User).filter(User.id == id).first()
    except SQLAlchemyError as e:
        logger.error(f"Database error fetching user {id}: {e}")
        raise UserNotFoundError(f"Could not fetch user {id}")
```

### JavaScript - Async Handling
```javascript
// Bad
function fetchData(url) {
    fetch(url).then(r => r.json()).then(console.log);
}

// Good
async function fetchData(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error(`Fetch failed: ${error.message}`);
        throw error;
    }
}
```

Remember to be constructive and educational in your feedback. Explain WHY something is an issue, not just WHAT the issue is.

You have extensive knowledge of:
- Languages: Python, JavaScript, TypeScript, Go, Rust, Java, C++
- Frameworks: React, Vue, Django, FastAPI, Express, Spring Boot
- Databases: PostgreSQL, MySQL, MongoDB, Redis, Elasticsearch
- Cloud: AWS, GCP, Azure, Kubernetes, Docker
- Tools: Git, CI/CD, Terraform, Ansible

Always provide actionable feedback with specific code examples when possible.
""" + "\n" * 100  # Padding to ensure >1024 tokens


def review_code_with_caching(code_snippets: List[str]) -> List[str]:
    """
    Review multiple code snippets using cached system prompt.

    First call: Cache write (+25% cost)
    Subsequent calls: Cache read (-90% cost!)
    """
    results = []

    for i, code in enumerate(code_snippets):
        print(f"\n📝 Reviewing snippet {i + 1}/{len(code_snippets)}...")

        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"}  # ← Enable caching!
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": f"Please review this code:\n\n```\n{code}\n```"
                }
            ]
        )

        # Check cache status from response headers/metadata if available
        results.append(response.content[0].text)

        # Print usage info
        usage = response.usage
        print(f"   Input tokens: {usage.input_tokens}")
        print(f"   Output tokens: {usage.output_tokens}")
        if hasattr(usage, 'cache_creation_input_tokens'):
            print(f"   Cache created: {usage.cache_creation_input_tokens} tokens")
        if hasattr(usage, 'cache_read_input_tokens'):
            print(f"   Cache read: {usage.cache_read_input_tokens} tokens ✅")

    return results


def main():
    # Example code snippets to review
    code_snippets = [
        """
def get_user(id):
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.execute(f"SELECT * FROM users WHERE id = {id}")
    return cursor.fetchone()
""",
        """
async function login(username, password) {
    const user = await db.findUser(username);
    if (user.password === password) {
        return { token: generateToken(user) };
    }
    return { error: 'Invalid credentials' };
}
""",
        """
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total
""",
    ]

    print("=" * 60)
    print("💰 Claude Prompt Caching Example")
    print("   Save up to 90% on repeated system prompts!")
    print("=" * 60)
    print(f"\n📋 System prompt size: ~{len(SYSTEM_PROMPT.split())} words")
    print(f"   Code snippets to review: {len(code_snippets)}")

    # Run reviews with caching
    results = review_code_with_caching(code_snippets)

    # Print results
    print("\n" + "=" * 60)
    print("📊 Review Results")
    print("=" * 60)

    for i, result in enumerate(results):
        print(f"\n--- Snippet {i + 1} Review ---")
        print(result[:500] + "..." if len(result) > 500 else result)

    # Cost comparison
    print("\n" + "=" * 60)
    print("💵 Cost Comparison (estimated)")
    print("=" * 60)

    system_tokens = 2000  # Approximate system prompt tokens
    input_tokens_per_request = 200  # User message tokens
    output_tokens = 500  # Response tokens
    num_requests = len(code_snippets)

    # Normal pricing
    normal_cost = (
        (system_tokens + input_tokens_per_request) * num_requests * 3 +
        output_tokens * num_requests * 15
    ) / 1_000_000

    # Cached pricing (first request writes, rest read)
    cached_cost = (
        # First request: cache write (+25%)
        system_tokens * 3.75 / 1_000_000 +
        input_tokens_per_request * 3 / 1_000_000 +
        output_tokens * 15 / 1_000_000 +
        # Subsequent requests: cache read (-90%)
        (num_requests - 1) * (
            system_tokens * 0.30 / 1_000_000 +  # 90% off!
            input_tokens_per_request * 3 / 1_000_000 +
            output_tokens * 15 / 1_000_000
        )
    )

    savings_pct = (1 - cached_cost / normal_cost) * 100

    print(f"  Normal API:  ${normal_cost:.4f}")
    print(f"  With Cache:  ${cached_cost:.4f}")
    print(f"  Savings:     ${normal_cost - cached_cost:.4f} ({savings_pct:.1f}%)")
    print(f"\n  💡 More requests = more savings!")
    print(f"     At 100 requests: ~{90}% savings")


if __name__ == "__main__":
    main()
