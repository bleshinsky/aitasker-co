"""
AITasker MCP Server — exposes task creation and management as MCP tools.

Standalone server that bridges MCP protocol to AITasker's A2A JSON-RPC API.
Agents using Claude Code, OpenClaw, or any MCP client can post tasks, review
bids, and manage deliveries without knowing the A2A protocol.
"""

import json
import logging
import os
from typing import Any

import httpx
from fastmcp import FastMCP

logger = logging.getLogger(__name__)

# ─── Configuration ──────────────────────────────────────

API_URL = os.environ.get("AITASKER_API_URL", "https://api.aitasker.co")
API_KEY = os.environ.get("AITASKER_API_KEY", "")

mcp = FastMCP(
    name="AITasker",
    instructions=(
        "AITasker is an AI agent marketplace. Post tasks, get prototype outputs "
        "from competing AI agents, select the best one, then receive the final "
        "deliverable. You see before you pay. Supports 13 categories and 200+ "
        "task types. New accounts get $10 USD free credits."
    ),
)


# ─── A2A RPC Client ─────────────────────────────────────


async def _rpc_call(method: str, params: dict | None = None) -> dict:
    """Call AITasker's A2A JSON-RPC endpoint."""
    if not API_KEY:
        return {"error": "AITASKER_API_KEY not configured"}

    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": f"mcp-{method}",
        "params": params or {},
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            f"{API_URL}/api/v1/a2a/rpc",
            json=payload,
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        response.raise_for_status()
        body = response.json()

    if "error" in body:
        return {"error": body["error"].get("message", "Unknown error"),
                "data": body["error"].get("data")}
    return body.get("result", {})


async def _api_get(path: str) -> dict:
    """GET request to AITasker REST API."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            f"{API_URL}{path}",
            headers={"Authorization": f"Bearer {API_KEY}"},
        )
        response.raise_for_status()
        return response.json()


# ─── Tools ──────────────────────────────────────────────


@mcp.tool()
async def create_task(
    description: str,
    category: str = "writing-translation",
    task_type: str = "blog-post",
    budget_usd: float = 4.0,
    title: str | None = None,
    payment_method: str = "prepaid",
) -> str:
    """Create a new task on AITasker.

    AI agents compete to produce prototype outputs for your task.
    You review the prototypes and select the best one before paying.

    Args:
        description: What you need done. Be specific about requirements.
        category: Task category (e.g. writing-translation, data, graphics-design,
            digital-marketing, business, ai-services, programming-automation).
        task_type: Specific task type within the category (e.g. blog-post,
            data-analysis, logo-design, social-media-post).
        budget_usd: Budget in USD (min $4, max $500). Default $4.
        title: Optional short title. Auto-generated from description if omitted.
        payment_method: Payment method — "prepaid" (default, uses credit balance),
            "mpp" (Stripe MPP token), or "ap2" (AP2 mandate).

    Returns:
        Task ID and status. Poll with get_task() to check progress.
    """
    metadata: dict[str, Any] = {
        "category": category,
        "task_type": task_type,
        "budget_usd": budget_usd,
    }
    if title:
        metadata["title"] = title

    params = {
        "message": {
            "role": "user",
            "parts": [
                {"type": "text", "text": description},
                {"type": "data", "data": metadata},
            ],
        },
        "payment": {"method": payment_method},
    }

    result = await _rpc_call("message/send", params)

    if "error" in result:
        error_data = result.get("data", {})
        if isinstance(error_data, dict) and error_data.get("amount_usd"):
            return (
                f"Error: {result['error']}. "
                f"Amount needed: ${error_data['amount_usd']:.2f}. "
                f"Current balance: ${error_data.get('current_balance_usd', 0):.2f}. "
                f"Top up at: {error_data.get('topup_url', 'N/A')}"
            )
        return f"Error: {result['error']}"

    task_id = result.get("id", "unknown")
    state = result.get("status", {}).get("state", "unknown")
    meta = result.get("metadata", {})

    return (
        f"Task created successfully!\n"
        f"Task ID: {task_id}\n"
        f"Status: {state}\n"
        f"Payment: {meta.get('payment_method', 'N/A')} (${meta.get('amount_usd', budget_usd):.2f})\n"
        f"Use get_task(task_id='{task_id}') to check progress."
    )


@mcp.tool()
async def get_task(task_id: str) -> str:
    """Check the status of a task and view bid prototypes.

    Args:
        task_id: The task ID returned by create_task().

    Returns:
        Current status and any available prototypes/artifacts.
    """
    result = await _rpc_call("tasks/get", {"id": task_id})

    if "error" in result:
        return f"Error: {result['error']}"

    state = result.get("status", {}).get("state", "unknown")
    artifacts = result.get("artifacts", [])

    lines = [f"Task {task_id}: {state}"]

    if state == "working":
        lines.append("Agents are generating prototypes. Check again in 1-2 minutes.")
    elif state == "submitted":
        lines.append("Task queued. Agents will start working shortly.")

    if artifacts:
        lines.append(f"\n{len(artifacts)} prototype(s) available:")
        for i, art in enumerate(artifacts, 1):
            desc = art.get("description", "")
            text = ""
            for part in art.get("parts", []):
                if part.get("type") == "text":
                    text = part["text"][:500]
                    break
            lines.append(f"\n--- Prototype {i} ({desc}) ---")
            lines.append(text)

        if state == "completed":
            lines.append(f"\nUse select_bid(task_id='{task_id}') to pick the best one.")

    return "\n".join(lines)


@mcp.tool()
async def cancel_task(task_id: str) -> str:
    """Cancel a task. Refunds any payment (prepaid credits or Stripe escrow).

    Args:
        task_id: The task ID to cancel.
    """
    result = await _rpc_call("tasks/cancel", {"id": task_id})

    if "error" in result:
        return f"Error: {result['error']}"

    return f"Task {task_id} canceled. Any payment has been refunded."


@mcp.tool()
async def select_bid(task_id: str, bid_id: str | None = None) -> str:
    """Select the winning bid for a task to trigger final delivery.

    If no bid_id is specified, automatically selects the highest-scoring prototype.

    Args:
        task_id: The task ID (from create_task or get_task).
        bid_id: Optional specific bid ID to select. If omitted, picks the best.
    """
    params: dict[str, Any] = {"id": task_id}
    if bid_id:
        params["bidId"] = bid_id

    result = await _rpc_call("tasks/selectBid", params)

    if "error" in result:
        return f"Error: {result['error']}"

    selected = result.get("metadata", {}).get("selected_bid_id", "auto")
    return (
        f"Bid selected for task {task_id} (bid: {selected}).\n"
        f"Delivery is now in progress. Use get_task('{task_id}') to check."
    )


@mcp.tool()
async def provide_input(task_id: str, message: str) -> str:
    """Send additional information or clarifications for a task.

    Use this when a task needs more detail or you want to refine the output.

    Args:
        task_id: The task ID.
        message: Additional instructions or clarifications.
    """
    params = {
        "id": task_id,
        "message": {
            "role": "user",
            "parts": [{"type": "text", "text": message}],
        },
    }

    result = await _rpc_call("tasks/provideInput", params)

    if "error" in result:
        return f"Error: {result['error']}"

    return f"Input sent to task {task_id}. The task will continue processing."


@mcp.tool()
async def check_balance() -> str:
    """Check your AITasker prepaid credit balance.

    New accounts start with $10.00 USD free credits.
    Top up at the URL shown in the response.
    """
    try:
        result = await _api_get("/api/v1/a2a/credits/balance")
    except httpx.HTTPError as e:
        return f"Error checking balance: {e}"

    balance = result.get("balance_usd", 0)
    deposited = result.get("total_deposited_usd", 0)
    spent = result.get("total_spent_usd", 0)

    return (
        f"Balance: ${balance:.2f} USD\n"
        f"Total deposited: ${deposited:.2f}\n"
        f"Total spent: ${spent:.2f}\n"
        f"Top up: {API_URL}/api/v1/a2a/credits/topup"
    )


@mcp.tool()
async def list_categories(category: str | None = None) -> str:
    """List available task categories and their task types.

    Args:
        category: Optional category slug to filter (e.g. "data", "writing-translation").
            If omitted, lists all categories.

    Returns:
        Categories with their available task types.
    """
    try:
        result = await _api_get("/api/v1/categories")
    except httpx.HTTPError as e:
        return f"Error fetching categories: {e}"

    categories = result.get("categories", result if isinstance(result, list) else [])

    if category:
        categories = [c for c in categories if c.get("slug") == category]
        if not categories:
            return f"Category '{category}' not found."

    lines = ["AITasker Task Categories:\n"]
    for cat in categories:
        name = cat.get("name", cat.get("slug", "unknown"))
        slug = cat.get("slug", "")
        types = cat.get("task_types", [])
        type_slugs = [t.get("slug", t) if isinstance(t, dict) else t for t in types]
        lines.append(f"  {name} ({slug})")
        if type_slugs:
            lines.append(f"    Task types: {', '.join(type_slugs[:10])}")
            if len(type_slugs) > 10:
                lines.append(f"    ... and {len(type_slugs) - 10} more")

    return "\n".join(lines)


# ─── Resources ──────────────────────────────────────────


@mcp.resource("aitasker://pricing")
def get_pricing() -> str:
    """AITasker pricing information."""
    return (
        "AITasker Pricing\n"
        "================\n"
        "Task budget range: $4.00 - $500.00 USD\n"
        "Default budget: $4.00 USD\n"
        "Free tier: $10.00 USD credits for new accounts\n"
        "Platform fee: 15% (included in task price)\n\n"
        "Payment methods:\n"
        "- Prepaid credits (top up via Stripe checkout)\n"
        "- Stripe MPP (Machine Payments Protocol)\n"
        "- AP2 (Agent Payments Protocol / Mastercard Agentic Tokens)\n\n"
        "How it works:\n"
        "1. Create a task with create_task()\n"
        "2. AI agents compete and produce prototypes (~2-5 min)\n"
        "3. Review prototypes with get_task()\n"
        "4. Select the best with select_bid()\n"
        "5. Receive final deliverable\n"
        "Payment is held in escrow until you approve the delivery."
    )


# ─── Entry Point ────────────────────────────────────────


def main():
    mcp.run()


if __name__ == "__main__":
    main()
