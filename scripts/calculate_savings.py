#!/usr/bin/env python3
"""
Cost Savings Calculator for Claude API

Calculate potential savings from Batch API, Prompt Caching,
and Extended Thinking optimizations.

Usage:
    python calculate_savings.py
    python calculate_savings.py --input 10000 --output 5000 --requests 100

Requirements:
    No external dependencies (stdlib only)
"""

import argparse
from dataclasses import dataclass
from typing import Optional


# Pricing as of January 2026 (per million tokens)
@dataclass
class Pricing:
    """Claude API pricing tiers."""
    # Sonnet 4.5
    SONNET_INPUT: float = 3.00
    SONNET_OUTPUT: float = 15.00
    SONNET_BATCH_INPUT: float = 1.50
    SONNET_BATCH_OUTPUT: float = 7.50
    SONNET_CACHE_WRITE: float = 3.75
    SONNET_CACHE_READ: float = 0.30

    # Opus 4.5
    OPUS_INPUT: float = 5.00
    OPUS_OUTPUT: float = 25.00
    OPUS_BATCH_INPUT: float = 2.50
    OPUS_BATCH_OUTPUT: float = 12.50

    # Haiku 4.5
    HAIKU_INPUT: float = 1.00
    HAIKU_OUTPUT: float = 5.00
    HAIKU_BATCH_INPUT: float = 0.50
    HAIKU_BATCH_OUTPUT: float = 2.50


def calculate_normal_cost(
    input_tokens: int,
    output_tokens: int,
    requests: int = 1,
    model: str = "sonnet"
) -> float:
    """Calculate cost without any optimization."""
    p = Pricing()

    if model == "sonnet":
        input_price = p.SONNET_INPUT
        output_price = p.SONNET_OUTPUT
    elif model == "opus":
        input_price = p.OPUS_INPUT
        output_price = p.OPUS_OUTPUT
    else:  # haiku
        input_price = p.HAIKU_INPUT
        output_price = p.HAIKU_OUTPUT

    cost = (
        input_tokens * requests * input_price +
        output_tokens * requests * output_price
    ) / 1_000_000

    return cost


def calculate_batch_cost(
    input_tokens: int,
    output_tokens: int,
    requests: int = 1,
    model: str = "sonnet"
) -> float:
    """Calculate cost with Batch API (50% off)."""
    p = Pricing()

    if model == "sonnet":
        input_price = p.SONNET_BATCH_INPUT
        output_price = p.SONNET_BATCH_OUTPUT
    elif model == "opus":
        input_price = p.OPUS_BATCH_INPUT
        output_price = p.OPUS_BATCH_OUTPUT
    else:  # haiku
        input_price = p.HAIKU_BATCH_INPUT
        output_price = p.HAIKU_BATCH_OUTPUT

    cost = (
        input_tokens * requests * input_price +
        output_tokens * requests * output_price
    ) / 1_000_000

    return cost


def calculate_cached_cost(
    input_tokens: int,
    output_tokens: int,
    system_tokens: int,
    requests: int = 1,
    model: str = "sonnet"
) -> float:
    """Calculate cost with Prompt Caching."""
    p = Pricing()

    if model != "sonnet":
        print("⚠️  Cache pricing shown for Sonnet. Other models may vary.")

    # First request: cache write
    first_request = (
        system_tokens * p.SONNET_CACHE_WRITE +
        input_tokens * p.SONNET_INPUT +
        output_tokens * p.SONNET_OUTPUT
    ) / 1_000_000

    # Subsequent requests: cache read
    subsequent = (requests - 1) * (
        system_tokens * p.SONNET_CACHE_READ +
        input_tokens * p.SONNET_INPUT +
        output_tokens * p.SONNET_OUTPUT
    ) / 1_000_000 if requests > 1 else 0

    return first_request + subsequent


def calculate_combined_cost(
    input_tokens: int,
    output_tokens: int,
    system_tokens: int,
    requests: int = 1
) -> float:
    """Calculate cost with both Batch API and Caching."""
    p = Pricing()

    # First request: cache write + batch pricing
    first_request = (
        system_tokens * p.SONNET_CACHE_WRITE +
        input_tokens * p.SONNET_BATCH_INPUT +
        output_tokens * p.SONNET_BATCH_OUTPUT
    ) / 1_000_000

    # Subsequent requests: cache read + batch pricing
    subsequent = (requests - 1) * (
        system_tokens * p.SONNET_CACHE_READ +
        input_tokens * p.SONNET_BATCH_INPUT +
        output_tokens * p.SONNET_BATCH_OUTPUT
    ) / 1_000_000 if requests > 1 else 0

    return first_request + subsequent


def print_report(
    input_tokens: int,
    output_tokens: int,
    system_tokens: int,
    requests: int,
    model: str = "sonnet"
) -> None:
    """Print a detailed savings report."""

    normal = calculate_normal_cost(input_tokens + system_tokens, output_tokens, requests, model)
    batch = calculate_batch_cost(input_tokens + system_tokens, output_tokens, requests, model)
    cached = calculate_cached_cost(input_tokens, output_tokens, system_tokens, requests, model)
    combined = calculate_combined_cost(input_tokens, output_tokens, system_tokens, requests)

    print("=" * 62)
    print("  💰 CLAUDE API COST SAVINGS REPORT")
    print("  🐾 by washinmura.jp")
    print("=" * 62)

    print(f"""
  📊 Your Usage:
     Model:           {model.capitalize()}
     Requests:        {requests:,}
     Input tokens:    {input_tokens:,} per request
     Output tokens:   {output_tokens:,} per request
     System prompt:   {system_tokens:,} tokens (cacheable)
""")

    print("  📈 Cost Comparison:")
    print("  ┌─────────────────────────────────────────────────────────┐")
    print(f"  │ {'Method':<20} │ {'Cost':>12} │ {'Savings':>10} │ {'%':>6} │")
    print("  ├─────────────────────────────────────────────────────────┤")
    print(f"  │ {'Normal API':<20} │ ${normal:>10.4f} │ {'—':>10} │ {'—':>6} │")
    print(f"  │ {'+ Batch API':<20} │ ${batch:>10.4f} │ ${normal-batch:>9.4f} │ {(1-batch/normal)*100:>5.1f}% │")
    print(f"  │ {'+ Prompt Caching':<20} │ ${cached:>10.4f} │ ${normal-cached:>9.4f} │ {(1-cached/normal)*100:>5.1f}% │")
    print(f"  │ {'+ Both (Maximum)':<20} │ ${combined:>10.4f} │ ${normal-combined:>9.4f} │ {(1-combined/normal)*100:>5.1f}% │")
    print("  └─────────────────────────────────────────────────────────┘")

    # Projections
    daily_requests = requests
    monthly = combined * 30
    yearly = combined * 365
    yearly_normal = normal * 365
    yearly_savings = yearly_normal - yearly

    print(f"""
  📅 Projections (at {daily_requests} requests/day):
     Daily:    ${combined:.2f}
     Monthly:  ${monthly:.2f}
     Yearly:   ${yearly:.2f}

  🎉 Yearly Savings: ${yearly_savings:.2f}
     (compared to ${yearly_normal:.2f} without optimization)
""")

    print("=" * 62)
    print("  💡 Tips:")
    print("     • Batch API: Best for tasks that can wait up to 24h")
    print("     • Caching: Best for repeated system prompts >1K tokens")
    print("     • Combined: Maximum savings for bulk processing")
    print("=" * 62)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate Claude API cost savings"
    )
    parser.add_argument(
        "--input", type=int, default=1000,
        help="Input tokens per request (excluding system prompt)"
    )
    parser.add_argument(
        "--output", type=int, default=500,
        help="Output tokens per request"
    )
    parser.add_argument(
        "--system", type=int, default=2000,
        help="System prompt tokens (cacheable)"
    )
    parser.add_argument(
        "--requests", type=int, default=100,
        help="Number of requests"
    )
    parser.add_argument(
        "--model", choices=["sonnet", "opus", "haiku"], default="sonnet",
        help="Claude model to use"
    )

    args = parser.parse_args()

    print_report(
        input_tokens=args.input,
        output_tokens=args.output,
        system_tokens=args.system,
        requests=args.requests,
        model=args.model
    )


if __name__ == "__main__":
    main()
