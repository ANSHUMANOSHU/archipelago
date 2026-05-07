"""Get financial metrics for a company."""

from pydantic import BaseModel, Field


class FinancialMetrics(BaseModel):
    """Financial metrics for a company."""

    symbol: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Company name")
    market_cap: float = Field(..., description="Market capitalization in billions")
    pe_ratio: float = Field(..., description="Price-to-earnings ratio")
    dividend_yield: float = Field(..., description="Dividend yield percentage")
    debt_to_equity: float = Field(..., description="Debt-to-equity ratio")
    current_ratio: float = Field(..., description="Current ratio")
    roe: float = Field(..., description="Return on equity percentage")
    roa: float = Field(..., description="Return on assets percentage")


async def get_financial_metrics(symbol: str) -> FinancialMetrics:
    """Get financial metrics for a company.

    Args:
        symbol: Stock ticker symbol (e.g., AAPL, MSFT)

    Returns:
        Financial metrics including valuation ratios, profitability, and leverage
    """
    # Stub implementation - returns mock data
    return FinancialMetrics(
        symbol=symbol,
        company_name="Example Corporation",
        market_cap=2850.5,
        pe_ratio=28.5,
        dividend_yield=1.2,
        debt_to_equity=0.45,
        current_ratio=1.85,
        roe=18.5,
        roa=12.3,
    )
