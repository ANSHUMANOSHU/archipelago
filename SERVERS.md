# Edgar SEC and FMP MCP Servers

## Overview

This document describes the implementation of Edgar SEC and FMP (Financial Market Platform) MCP servers for the Archipelago system.

## Problem Statement

The HuggingFace dataset contains worlds that reference "Edgar SEC" and "FMP" MCP servers in their `apps` field. However:
- These servers were not implemented in the `mcp_servers/` directory
- They were not included in `mcp_config_all_oss_servers.json`
- Tasks in financial/investment-banking domains that depend on these tools would fail silently

## Solution

Implemented stub servers with realistic mock data, enhanced validation, and clear error handling.

---

## Edgar SEC Server

### Location
`mcp_servers/edgar/`

### Tools

#### search_filings
Search for SEC filings by company, CIK, or filing type.

**Parameters:**
- `company_name` (optional): Company name to search for
- `cik` (optional): Central Index Key (CIK) of the company
- `filing_type` (optional): Type of filing (10-K, 10-Q, 8-K, S-1, etc.)
- `start_date` (optional): Start date for search (YYYY-MM-DD)
- `end_date` (optional): End date for search (YYYY-MM-DD)
- `limit` (optional): Maximum number of results (default: 10)

**Returns:** List of FilingResult objects with accession_number, company_name, cik, filing_type, filing_date, period_of_report, url

#### get_filing
Retrieve a specific SEC filing document by accession number.

**Parameters:**
- `accession_number`: SEC accession number (e.g., 0001193125-24-001234)

**Returns:** FilingDocument object with accession_number, company_name, filing_type, filing_date, content_preview, full_text_url

#### get_company_info
Get company information from the SEC database.

**Parameters:**
- `cik`: Central Index Key (CIK) of the company

**Returns:** CompanyInfo object with cik, company_name, sic_code, sic_description, state_of_incorporation, business_address, phone

### Status
Stub implementation with mock data. Production version would connect to SEC EDGAR API.

---

## FMP Server

### Location
`mcp_servers/fmp/`

### Tools

#### get_stock_price
Get stock price data for a given ticker symbol.

**Parameters:**
- `symbol`: Stock ticker symbol (e.g., AAPL, MSFT)
- `date` (optional): Specific date to retrieve (YYYY-MM-DD)
- `period` (optional): Time period for historical data (1d, 1w, 1m, 3m, 6m, 1y, 5y)

**Returns:** List of StockPrice objects with symbol, price, date, open, high, low, close, volume

#### get_financial_metrics
Get financial metrics for a company.

**Parameters:**
- `symbol`: Stock ticker symbol (e.g., AAPL, MSFT)

**Returns:** FinancialMetrics object with symbol, company_name, market_cap, pe_ratio, dividend_yield, debt_to_equity, current_ratio, roe, roa

#### get_market_data
Get market data and indices.

**Parameters:**
- `index` (optional): Market index to retrieve (SP500, NASDAQ, DOW, VIX, etc.)

**Returns:** List of MarketData objects with index_name, symbol, value, change, change_percent, date

### Status
Stub implementation with mock data. Production version would connect to FMP API.

---

## Configuration

### MCP Config File
`examples/hugging_face_task/mcp_config_all_oss_servers.json`

Both servers are configured with:
- Transport: stdio
- Command: uv run python main.py
- Working directory: /app/mcp_servers/{edgar|fmp}/mcp_servers/{edgar|fmp}_server

### Server Validation
When running tasks, the system:
1. Logs available servers
2. Logs required servers for the world
3. Warns about missing servers
4. Notes when stub implementations are being used (only if both required and configured)

Example output:
```
[14:30:45] Configuring MCP servers...
[14:30:45]   Available servers: [..., 'edgar_server', 'fmp_server', ...]
[14:30:45]   Required servers: ['edgar_server', 'fmp_server', 'filesystem_server']
[14:30:45]   NOTE: Using stub implementations for: ['edgar_server', 'fmp_server']
[14:30:45]   These servers provide mock data for development/testing
```

---

## Implementation Details

### Files Created

**Edgar Server (7 files)**
- `mcp_servers/edgar/pyproject.toml` - Project configuration
- `mcp_servers/edgar/README.md` - Server documentation
- `mcp_servers/edgar/mcp_servers/edgar_server/main.py` - Server entry point
- `mcp_servers/edgar/mcp_servers/edgar_server/tools/__init__.py` - Package marker
- `mcp_servers/edgar/mcp_servers/edgar_server/tools/search_filings.py` - Search tool
- `mcp_servers/edgar/mcp_servers/edgar_server/tools/get_filing.py` - Retrieval tool
- `mcp_servers/edgar/mcp_servers/edgar_server/tools/get_company_info.py` - Company info tool

**FMP Server (7 files)**
- `mcp_servers/fmp/pyproject.toml` - Project configuration
- `mcp_servers/fmp/README.md` - Server documentation
- `mcp_servers/fmp/mcp_servers/fmp_server/main.py` - Server entry point
- `mcp_servers/fmp/mcp_servers/fmp_server/tools/__init__.py` - Package marker
- `mcp_servers/fmp/mcp_servers/fmp_server/tools/get_stock_price.py` - Stock price tool
- `mcp_servers/fmp/mcp_servers/fmp_server/tools/get_financial_metrics.py` - Metrics tool
- `mcp_servers/fmp/mcp_servers/fmp_server/tools/get_market_data.py` - Market data tool

### Files Modified

**examples/hugging_face_task/main.py**
- Added server validation logic
- Enhanced logging for available/required servers
- Fixed stub detection to verify servers are both required and configured

**examples/hugging_face_task/mcp_config_all_oss_servers.json**
- Added edgar_server configuration
- Added fmp_server configuration

---

## Usage

### Running a Financial Task

```bash
cd examples/hugging_face_task
./run.sh task_43a921f91f0f4d2c85d8bd2774f9e681
```

The system will:
1. Load all 11 MCP servers
2. Detect that the world requires edgar_server and fmp_server
3. Log that stub implementations are being used
4. Run the agent with access to mock financial data

### Testing Servers Locally

```bash
# Test Edgar server
cd mcp_servers/edgar
uv sync
uv run python -m mcp_servers.edgar_server.main

# Test FMP server
cd mcp_servers/fmp
uv sync
uv run python -m mcp_servers.fmp_server.main
```

---

## Production Roadmap

### Edgar SEC Server
To implement production version:
1. Integrate with SEC EDGAR API (https://www.sec.gov/cgi-bin/browse-edgar)
2. Add caching layer for frequently accessed filings
3. Implement XBRL data extraction
4. Add proper error handling for API rate limits
5. Implement full-text search capabilities

### FMP Server
To implement production version:
1. Integrate with FMP API (https://financialmodelingprep.com/)
2. Add API key management and authentication
3. Implement caching for frequently accessed data
4. Add support for real-time data streaming
5. Implement proper error handling for API rate limits

**Important**: Both servers follow the same MCP interface, so agent code doesn't need to change when switching from stub to production implementations.

---

## Troubleshooting

### Server Not Loading
- Check that the server directory exists at the configured path
- Verify the `cwd` in the MCP config is correct
- Check server logs for startup errors

### Missing Tools
- Verify the server is registered in the MCP config
- Check that tools are properly decorated with `@mcp.tool()`
- Review server logs for tool registration errors

### Stub Data Issues
- Stub servers return consistent mock data for testing
- For production data, implement the real API integration
- Contact the development team for production server implementations

---

## References

- [SEC EDGAR API Documentation](https://www.sec.gov/cgi-bin/browse-edgar)
- [FMP API Documentation](https://financialmodelingprep.com/api/)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

---

## Summary

- ✅ Edgar SEC server implemented with 3 tools
- ✅ FMP server implemented with 3 tools
- ✅ Both servers added to MCP configuration
- ✅ Enhanced validation and logging
- ✅ Clear production roadmap
- ✅ Ready for immediate use
