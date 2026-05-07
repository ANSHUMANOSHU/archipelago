"""Search for SEC filings."""

from typing import Optional

from pydantic import BaseModel, Field


class FilingResult(BaseModel):
    """A SEC filing result."""

    accession_number: str = Field(..., description="SEC accession number")
    company_name: str = Field(..., description="Company name")
    cik: str = Field(..., description="Central Index Key")
    filing_type: str = Field(..., description="Type of filing (10-K, 10-Q, 8-K, etc.)")
    filing_date: str = Field(..., description="Date of filing (YYYY-MM-DD)")
    period_of_report: Optional[str] = Field(None, description="Period covered by the filing")
    url: str = Field(..., description="URL to the filing document")


async def search_filings(
    company_name: Optional[str] = None,
    cik: Optional[str] = None,
    filing_type: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: int = 10,
) -> list[FilingResult]:
    """Search for SEC filings.

    Args:
        company_name: Company name to search for
        cik: Central Index Key (CIK) of the company
        filing_type: Type of filing (10-K, 10-Q, 8-K, S-1, etc.)
        start_date: Start date for search (YYYY-MM-DD)
        end_date: End date for search (YYYY-MM-DD)
        limit: Maximum number of results to return (default: 10)

    Returns:
        List of filing results matching the search criteria
    """
    # Stub implementation - returns mock data
    mock_filings = [
        FilingResult(
            accession_number="0001193125-24-001234",
            company_name=company_name or "Example Corp",
            cik=cik or "0000789019",
            filing_type=filing_type or "10-K",
            filing_date="2024-02-15",
            period_of_report="2023-12-31",
            url="https://www.sec.gov/cgi-bin/viewer?action=view&cik=789019&accession_number=0001193125-24-001234",
        ),
        FilingResult(
            accession_number="0001193125-23-456789",
            company_name=company_name or "Example Corp",
            cik=cik or "0000789019",
            filing_type=filing_type or "10-Q",
            filing_date="2023-11-15",
            period_of_report="2023-09-30",
            url="https://www.sec.gov/cgi-bin/viewer?action=view&cik=789019&accession_number=0001193125-23-456789",
        ),
    ]
    return mock_filings[:limit]
