#!/usr/bin/env python3
"""
Batch API Example - Save 50% on Claude API costs

This script demonstrates how to use Claude's Batch API
for non-urgent tasks that can wait up to 24 hours.

Usage:
    python batch_example.py

Requirements:
    pip install anthropic
"""

import anthropic
import time
from typing import List, Dict

# Initialize client
client = anthropic.Anthropic()


def create_batch_requests(tasks: List[str]) -> List[Dict]:
    """Convert a list of tasks into batch request format."""
    return [
        {
            "custom_id": f"task-{i:03d}",
            "params": {
                "model": "claude-sonnet-4-5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": task}]
            }
        }
        for i, task in enumerate(tasks)
    ]


def submit_batch(tasks: List[str]) -> str:
    """Submit a batch of tasks and return the batch ID."""
    requests = create_batch_requests(tasks)

    batch = client.messages.batches.create(requests=requests)

    print(f"✅ Batch created: {batch.id}")
    print(f"   Status: {batch.processing_status}")
    print(f"   Requests: {len(requests)}")

    return batch.id


def wait_for_completion(batch_id: str, poll_interval: int = 30) -> None:
    """Poll until the batch is complete."""
    print(f"\n⏳ Waiting for batch {batch_id} to complete...")

    while True:
        batch = client.messages.batches.retrieve(batch_id)
        status = batch.processing_status

        if status == "ended":
            print(f"✅ Batch completed!")
            print(f"   Succeeded: {batch.request_counts.succeeded}")
            print(f"   Failed: {batch.request_counts.errored}")
            break

        print(f"   Status: {status} - waiting {poll_interval}s...")
        time.sleep(poll_interval)


def get_results(batch_id: str) -> List[Dict]:
    """Retrieve results from a completed batch."""
    results = []

    for result in client.messages.batches.results(batch_id):
        results.append({
            "id": result.custom_id,
            "status": result.result.type,
            "content": result.result.message.content[0].text
            if result.result.type == "succeeded" else None
        })

    return results


def main():
    # Example tasks - replace with your actual tasks
    tasks = [
        "Summarize the benefits of renewable energy in 2 sentences.",
        "What is the capital of France? Answer in one word.",
        "List 3 programming languages used for AI development.",
        "Explain photosynthesis to a 5-year-old in one sentence.",
        "What year did the first iPhone release? Just the year.",
    ]

    print("=" * 50)
    print("💰 Claude Batch API Example")
    print("   Save 50% on API costs for non-urgent tasks!")
    print("=" * 50)

    # Submit batch
    batch_id = submit_batch(tasks)

    # Wait for completion
    wait_for_completion(batch_id)

    # Get results
    print("\n📋 Results:")
    print("-" * 50)

    results = get_results(batch_id)
    for r in results:
        print(f"\n[{r['id']}]")
        print(f"  {r['content']}")

    # Cost comparison
    print("\n" + "=" * 50)
    print("💵 Cost Comparison (estimated)")
    print("=" * 50)

    # Rough estimates (adjust based on actual token counts)
    input_tokens = 500 * len(tasks)  # ~100 tokens per task
    output_tokens = 250 * len(tasks)  # ~50 tokens per response

    normal_cost = (input_tokens * 3 + output_tokens * 15) / 1_000_000
    batch_cost = (input_tokens * 1.5 + output_tokens * 7.5) / 1_000_000

    print(f"  Normal API:  ${normal_cost:.4f}")
    print(f"  Batch API:   ${batch_cost:.4f}")
    print(f"  Savings:     ${normal_cost - batch_cost:.4f} ({50}%)")


if __name__ == "__main__":
    main()
