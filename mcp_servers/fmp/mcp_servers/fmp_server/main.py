"""FMP (Financial Market Platform) MCP Server.

Provides access to financial market data, stock prices, and company financial metrics.
This is a stub implementation that provides mock data for development and testing.

Tools:
- get_stock_price: Get current or historical stock prices
- get_financial_metrics: Get financial metrics for a company
- get_market_data: Get market data and indices
"""

import os

from fastmcp import FastMCP

mcp = FastMCP(
    "fmp-server",
    instructions="Financial Market Platform (FMP) data access for stock prices, financial metrics, market data, and company information. Get real-time and historical stock prices, financial ratios, earnings data, and market indices. Stub implementation for development.",
)

if __name__ == "__main__":
    from tools.get_stock_price import get_stock_price
    from tools.get_financial_metrics import get_financial_metrics
    from tools.get_market_data import get_market_data

    mcp.tool(get_stock_price)
    mcp.tool(get_financial_metrics)
    mcp.tool(get_market_data)

    transport = os.getenv("MCP_TRANSPORT", "http").lower()
    if transport == "http":
        port = int(os.getenv("MCP_PORT", "5000"))
        mcp.run(transport="http", host="0.0.0.0", port=port)
    else:
        mcp.run(transport="stdio")
