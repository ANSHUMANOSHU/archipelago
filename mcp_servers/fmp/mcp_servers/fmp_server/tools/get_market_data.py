"""Get market data and indices."""

from pydantic import BaseModel, Field


class MarketData(BaseModel):
    """Market data and indices."""

    index_name: str = Field(..., description="Name of the market index")
    symbol: str = Field(..., description="Index symbol (e.g., ^GSPC for S&P 500)")
    value: float = Field(..., description="Current index value")
    change: float = Field(..., description="Change in points")
    change_percent: float = Field(..., description="Percentage change")
    date: str = Field(..., description="Date of the data (YYYY-MM-DD)")


async def get_market_data(index: str = "SP500") -> list[MarketData]:
    """Get market data and indices.

    Args:
        index: Market index to retrieve (SP500, NASDAQ, DOW, VIX, etc.)

    Returns:
        Market data including index value and changes
    """
    # Stub implementation - returns mock data
    index_map = {
        "SP500": ("S&P 500", "^GSPC", 5234.80),
        "NASDAQ": ("NASDAQ Composite", "^IXIC", 16432.50),
        "DOW": ("Dow Jones Industrial Average", "^DJI", 39512.25),
        "VIX": ("Volatility Index", "^VIX", 14.25),
    }

    index_name, symbol, value = index_map.get(index, ("S&P 500", "^GSPC", 5234.80))

    return [
        MarketData(
            index_name=index_name,
            symbol=symbol,
            value=value,
            change=45.50,
            change_percent=0.87,
            date="2024-05-07",
        ),
    ]
