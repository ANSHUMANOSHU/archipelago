"""Edgar SEC MCP Server.

Provides access to SEC filing data through the EDGAR database.
This is a stub implementation that provides mock data for development and testing.

Tools:
- search_filings: Search for SEC filings by company, CIK, or filing type
- get_filing: Retrieve a specific SEC filing document
- get_company_info: Get company information from SEC database
"""

import os

from fastmcp import FastMCP

mcp = FastMCP(
    "edgar-server",
    instructions="SEC EDGAR database access for retrieving company filings, financial reports, and regulatory documents. Search filings by company name, CIK, or filing type (10-K, 10-Q, 8-K, etc.). Retrieve full filing documents and extract financial data. Stub implementation for development.",
)

if __name__ == "__main__":
    from tools.search_filings import search_filings
    from tools.get_filing import get_filing
    from tools.get_company_info import get_company_info

    mcp.tool(search_filings)
    mcp.tool(get_filing)
    mcp.tool(get_company_info)

    transport = os.getenv("MCP_TRANSPORT", "http").lower()
    if transport == "http":
        port = int(os.getenv("MCP_PORT", "5000"))
        mcp.run(transport="http", host="0.0.0.0", port=port)
    else:
        mcp.run(transport="stdio")
