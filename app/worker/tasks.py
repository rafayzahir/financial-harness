
from app.services.market_data.finnhub import get_quote
from app.worker.celery_app import celery_app


@celery_app.task(
    bind=True,
    name="app.worker.tasks.fetch_market_quote",
)
def fetch_market_quote(self, symbol: str):
    symbol = symbol.strip().upper()

    if not symbol:
        raise ValueError("Stock symbol cannot be empty")

    quote = get_quote(symbol)

    return {
        "symbol": symbol,
        "quote": quote,
        "source": "Finnhub",
    }
