"""Tests for select_bid, provide_input, check_balance tools."""
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_select_bid_auto():
    from server import select_bid

    mock_result = {
        "id": "a2a-123",
        "status": {"state": "working"},
        "metadata": {"selected_bid_id": "bid-456"},
    }

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await select_bid(task_id="a2a-123")

    assert "bid-456" in result or "selected" in result.lower()


@pytest.mark.asyncio
async def test_provide_input():
    from server import provide_input

    mock_result = {"id": "a2a-123", "status": {"state": "working"}}

    with patch("server._rpc_call", new_callable=AsyncMock, return_value=mock_result):
        result = await provide_input(task_id="a2a-123", message="Use formal tone")

    assert "a2a-123" in result


@pytest.mark.asyncio
async def test_check_balance():
    from server import check_balance

    mock_response = {
        "caller_id": "user-1",
        "balance_usd": 6.0,
        "total_deposited_usd": 10.0,
        "total_spent_usd": 4.0,
    }

    with patch("server._api_get", new_callable=AsyncMock, return_value=mock_response):
        result = await check_balance()

    assert "$6.00" in result
