# FMP (Financial Market Platform) MCP Server

A Python-based MCP server for accessing financial market data and company financial metrics.

## Overview

This server provides tools for retrieving stock prices, financial metrics, and market data from the Financial Market Platform (FMP).

## Tools

### get_stock_price
Get stock price data for a given ticker symbol.

**Parameters:**
- `symbol`: Stock ticker symbol (e.g., AAPL, MSFT)
- `date` (optional): Specific date to retrieve (YYYY-MM-DD)
- `period` (optional): Time period for historical data (1d, 1w, 1m, 3m, 6m, 1y, 5y)

### get_financial_metrics
Get financial metrics for a company.

**Parameters:**
- `symbol`: Stock ticker symbol (e.g., AAPL, MSFT)

### get_market_data
Get market data and indices.

**Parameters:**
- `index` (optional): Market index to retrieve (SP500, NASDAQ, DOW, VIX, etc.)

## Note

This is a stub implementation for development and testing. In a production environment, this server would connect to the actual FMP API to retrieve real market data.

## Development

```bash
# Install dependencies
uv sync

# Run the server
uv run python main.py
```
