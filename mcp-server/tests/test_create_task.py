"""Tests for create_task MCP tool."""
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_create_task_calls_rpc():
    """create_task sends message/send to A2A RPC."""
    from server import create_task

    mock_result = {
        "id": "a2a-task-123",
        "status": {"state": "submitted"},
        "metadata": {"task_id": "uuid-456", "payment_method": "prepaid"},
    }

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await create_task(
            description="Write a blog post about AI trends",
            category="writing-translation",
            task_type="blog-post",
        )

    assert "a2a-task-123" in result
    assert "submitted" in result


@pytest.mark.asyncio
async def test_create_task_with_budget():
    """create_task passes budget to A2A RPC."""
    from server import create_task

    mock_result = {"id": "a2a-task-456", "status": {"state": "submitted"}, "metadata": {}}

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result) as mock_rpc:
        await create_task(
            description="Analyze sales data",
            category="data",
            task_type="data-analysis",
            budget_usd=15.0,
        )

    call_params = mock_rpc.call_args[0][1]
    metadata = call_params["message"]["parts"][1]["data"]
    assert metadata["budget_usd"] == 15.0


@pytest.mark.asyncio
async def test_create_task_error():
    """create_task returns error message on failure."""
    from server import create_task

    with patch("server._rpc_call", new_callable=AsyncMock, return_value={"error": "Payment required"}):
        result = await create_task(description="test")

    assert "error" in result.lower() or "payment" in result.lower()
