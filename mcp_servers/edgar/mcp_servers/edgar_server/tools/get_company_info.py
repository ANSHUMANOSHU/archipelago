"""Get company information from SEC database."""

from pydantic import BaseModel, Field


class CompanyInfo(BaseModel):
    """Company information from SEC database."""

    cik: str = Field(..., description="Central Index Key")
    company_name: str = Field(..., description="Official company name")
    sic_code: str = Field(..., description="Standard Industrial Classification code")
    sic_description: str = Field(..., description="SIC industry description")
    state_of_incorporation: str = Field(..., description="State where company is incorporated")
    business_address: str = Field(..., description="Business address")
    phone: str = Field(..., description="Phone number")


async def get_company_info(cik: str) -> CompanyInfo:
    """Get company information from SEC database.

    Args:
        cik: Central Index Key (CIK) of the company

    Returns:
        Company information including CIK, name, SIC code, and contact details
    """
    # Stub implementation - returns mock data
    return CompanyInfo(
        cik=cik,
        company_name="Example Corporation",
        sic_code="3721",
        sic_description="Aircraft",
        state_of_incorporation="DE",
        business_address="123 Main Street, New York, NY 10001",
        phone="(212) 555-0100",
    )
