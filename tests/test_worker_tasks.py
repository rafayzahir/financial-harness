
from unittest.mock import patch

import pytest

from app.worker.tasks import fetch_market_quote


def test_fetch_market_quote():
    mock_quote = {
        "c": 150.0,
        "h": 155.0,
        "l": 148.0,
        "o": 149.0,
        "pc": 147.0,
    }

    with patch(
        "app.worker.tasks.get_quote",
        return_value=mock_quote,
    ) as mocked_get_quote:
        result = fetch_market_quote.run("aapl")

    mocked_get_quote.assert_called_once_with("AAPL")

    assert result["symbol"] == "AAPL"
    assert result["quote"] == mock_quote
    assert result["source"] == "Finnhub"


def test_fetch_market_quote_rejects_empty_symbol():
    with patch("app.worker.tasks.get_quote") as mocked_get_quote:
        with pytest.raises(ValueError):
            fetch_market_quote.run("   ")

    mocked_get_quote.assert_not_called()
