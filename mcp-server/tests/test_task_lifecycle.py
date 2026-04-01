"""Tests for get_task and cancel_task MCP tools."""
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_get_task_returns_status():
    from server import get_task

    mock_result = {
        "id": "a2a-123",
        "status": {"state": "working"},
        "artifacts": [],
    }

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await get_task(task_id="a2a-123")

    assert "working" in result


@pytest.mark.asyncio
async def test_get_task_with_artifacts():
    from server import get_task

    mock_result = {
        "id": "a2a-123",
        "status": {"state": "completed"},
        "artifacts": [
            {"name": "prototype-1", "description": "Score: 0.85",
             "parts": [{"type": "text", "text": "Blog post about AI..."}]}
        ],
    }

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await get_task(task_id="a2a-123")

    assert "completed" in result
    assert "prototype" in result.lower() or "Blog post" in result


@pytest.mark.asyncio
async def test_cancel_task():
    from server import cancel_task

    mock_result = {"id": "a2a-123", "status": {"state": "canceled"}}

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await cancel_task(task_id="a2a-123")

    assert "canceled" in result.lower()
