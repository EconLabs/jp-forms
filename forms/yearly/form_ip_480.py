from sqlmodel import Field, SQLModel
from typing import Optional

class IP480Validator(SQLModel, table=True):
    """
    Schema for IP-480 Validator form

    Parameters:
    -----------
    **args: Arguments given by the form

    Returns:
    --------
    None
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str
    address: str
    email: str
    liaison_officer: str
    ssn: str
    tel: str
    fax: str
    legal_form: str
    cfc: str
    business_function: str
    closing_date: str
    start_year: int
    end_year: int

    operation_incomes_1: float
    operation_incomes_2: float
    people_A_1: float
    people_A_2: float
    industries_businesses_A_1: float
    industries_businesses_A_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_rents_1: float
    incomes_rents_2: float
    dividends_1: float
    dividends_2: float
    others_incomes_1: float
    others_incomes_2: float
    total_incomes_1: float
    total_incomes_2: float

    salaries_1: float
    salaries_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rents_1: float
    expenses_rents_2: float
    depreciation_1: float
    depreciation_2: float
    donations_1: float
    donations_2: float
    sales_tax_1: float
    sales_tax_2: float
    machinery_1: float
    machinery_2: float
    other_purchases_1: float
    other_purchases_2: float
    licenses_1: float
    licenses_2: float
    other_expenses_1: float
    other_expenses_2: float
    total_expenses_1: float
    total_expenses_2: float

    net_profit_1: float
    net_profit_2: float
    income_tax_1: float
    income_tax_2: float
    profit_after_tax_1: float
    profit_after_tax_2: float
    withheld_tax_1: float
    withheld_tax_2: float

    signature: str
    rank: str