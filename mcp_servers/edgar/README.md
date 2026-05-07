# Edgar SEC MCP Server

A Python-based MCP server for accessing SEC EDGAR filing data.

## Overview

This server provides tools for searching and retrieving SEC filings, company information, and financial documents from the EDGAR database.

## Tools

### search_filings
Search for SEC filings by company name, CIK, or filing type.

**Parameters:**
- `company_name` (optional): Company name to search for
- `cik` (optional): Central Index Key (CIK) of the company
- `filing_type` (optional): Type of filing (10-K, 10-Q, 8-K, S-1, etc.)
- `start_date` (optional): Start date for search (YYYY-MM-DD)
- `end_date` (optional): End date for search (YYYY-MM-DD)
- `limit` (optional): Maximum number of results (default: 10)

### get_filing
Retrieve a specific SEC filing document by accession number.

**Parameters:**
- `accession_number`: SEC accession number (e.g., 0001193125-24-001234)

### get_company_info
Get company information from the SEC database.

**Parameters:**
- `cik`: Central Index Key (CIK) of the company

## Note

This is a stub implementation for development and testing. In a production environment, this server would connect to the actual SEC EDGAR API to retrieve real filing data.

## Development

```bash
# Install dependencies
uv sync

# Run the server
uv run python main.py
```
