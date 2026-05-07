"""Get stock price data."""

from typing import Optional

from pydantic import BaseModel, Field


class StockPrice(BaseModel):
    """Stock price data."""

    symbol: str = Field(..., description="Stock ticker symbol")
    price: float = Field(..., description="Current or historical price")
    date: str = Field(..., description="Date of the price (YYYY-MM-DD)")
    open: Optional[float] = Field(None, description="Opening price")
    high: Optional[float] = Field(None, description="High price")
    low: Optional[float] = Field(None, description="Low price")
    close: Optional[float] = Field(None, description="Closing price")
    volume: Optional[int] = Field(None, description="Trading volume")


async def get_stock_price(
    symbol: str,
    date: Optional[str] = None,
    period: str = "1d",
) -> list[StockPrice]:
    """Get stock price data.

    Args:
        symbol: Stock ticker symbol (e.g., AAPL, MSFT)
        date: Specific date to retrieve (YYYY-MM-DD). If not provided, returns latest
        period: Time period for historical data (1d, 1w, 1m, 3m, 6m, 1y, 5y)

    Returns:
        List of stock price data points
    """
    # Stub implementation - returns mock data
    return [
        StockPrice(
            symbol=symbol,
            price=150.25,
            date=date or "2024-05-07",
            open=149.50,
            high=151.75,
            low=149.25,
            close=150.25,
            volume=52_000_000,
        ),
        StockPrice(
            symbol=symbol,
            price=149.75,
            date="2024-05-06",
            open=150.00,
            high=150.50,
            low=149.00,
            close=149.75,
            volume=48_500_000,
        ),
    ]
