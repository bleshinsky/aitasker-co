"""Tests for list_categories tool and resources."""
import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_list_categories():
    from server import list_categories

    mock_response = {
        "categories": [
            {"slug": "writing-translation", "name": "Writing & Translation",
             "task_types": ["blog-post", "article", "copywriting"]},
            {"slug": "data", "name": "Data",
             "task_types": ["data-analysis", "spreadsheet"]},
        ]
    }

    with patch("server._api_get", new_callable=AsyncMock, return_value=mock_response):
        result = await list_categories()

    assert "writing" in result.lower()
    assert "data" in result.lower()
