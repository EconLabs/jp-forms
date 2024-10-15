from sqlmodel import Field, SQLModel
from typing import Optional

class IP490Validator(SQLModel, table=True):
    """
    Schema for IP-490 Validator form

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
    business_type: str
    business_function: str
    closing_date: str
    start_year: int
    end_year: int

    income_operations_1: float
    income_operations_2: float
    people_A_1: float
    people_A_2: float
    industries_businesses_A_1: float
    industries_businesses_A_2: float
    interest_A_1: float
    interest_A_2: float
    rent_land_1: float
    rent_land_2: float
    capital_gain_1: float
    capital_gain_2: float
    other_income_A_1: float
    other_income_A_2: float
    total_income_A_1: float
    total_income_A_2: float
    salaries_wages_bonus_B_1: float
    salaries_wages_bonus_B_2: float
    interests_B_1: float
    interests_B_2: float
    rent_B_1: float
    rent_B_2: float
    depreciation_B_1: float
    depreciation_B_2: float
    donation_B_1: float
    donation_B_2: float
    sales_taxes_B_1: float
    sales_taxes_B_2: float
    purchases_B_1: float
    purchases_B_2: float
    other_purchases_B_1: float
    other_purchases_B_2: float
    other_operations_B_1: float
    other_operations_B_2: float
    total_expenses_B_1: float
    total_expenses_B_2: float
    net_profit_1: float
    net_profit_2: float
    income_C_1: float
    income_C_2: float
    profit_C_after_1: float
    profit_C_after_2: float
    sales_D_1: float
    sales_D_2: float

    name: str
    rank: str