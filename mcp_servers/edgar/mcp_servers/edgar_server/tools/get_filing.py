"""Get a specific SEC filing."""

from pydantic import BaseModel, Field


class FilingDocument(BaseModel):
    """A SEC filing document."""

    accession_number: str = Field(..., description="SEC accession number")
    company_name: str = Field(..., description="Company name")
    filing_type: str = Field(..., description="Type of filing")
    filing_date: str = Field(..., description="Date of filing")
    content_preview: str = Field(..., description="Preview of filing content")
    full_text_url: str = Field(..., description="URL to full text")


async def get_filing(accession_number: str) -> FilingDocument:
    """Retrieve a specific SEC filing document.

    Args:
        accession_number: SEC accession number (e.g., 0001193125-24-001234)

    Returns:
        Filing document with content preview and metadata
    """
    # Stub implementation - returns mock data
    return FilingDocument(
        accession_number=accession_number,
        company_name="Example Corp",
        filing_type="10-K",
        filing_date="2024-02-15",
        content_preview="This is a mock filing document. In a production environment, this would contain the actual SEC filing content including financial statements, management discussion and analysis, and other regulatory disclosures.",
        full_text_url=f"https://www.sec.gov/cgi-bin/viewer?action=view&accession_number={accession_number}",
    )
