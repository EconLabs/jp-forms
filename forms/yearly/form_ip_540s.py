from sqlmodel import Field, SQLModel
from typing import Optional

class IP540SValidator(SQLModel, table=True):
    """
    Schema for IP-540S Validator form
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

    incomes_from_persons_1: float
    incomes_from_persons_2: float
    incomes_from_industries_and_businesses_1: float
    incomes_from_industries_and_businesses_2: float

    expenses_newspapers_1: float
    expenses_newspapers_2: float
    expenses_radio_1: float
    expenses_radio_2: float
    expenses_other_1: float
    expenses_other_2: float
    gross_profit_1: float
    gross_profit_2: float
    gross_other_income_1: float
    gross_other_income_2: float
    gross_interests_1: float
    gross_interests_2: float
    gross_rent_land_1: float
    gross_rent_land_2: float
    gross_capital_gain_1: float
    gross_capital_gain_2: float
    gross_other_1: float
    gross_other_2: float

    income_total_income_1: float
    income_total_income_2: float
    income_total_expenses_1: float
    income_total_expenses_2: float

    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_other_taxes_1: float
    expenses_other_taxes_2: float
    expenses_donations_1: float
    expenses_donations_2: float
    expenses_sales_taxes_1: float
    expenses_sales_taxes_2: float
    expenses_purchases_machinery_1: float
    expenses_purchases_machinery_2: float
    expenses_other_purchases_1: float
    expenses_other_purchases_2: float
    expenses_licenses_1: float
    expenses_licenses_2: float
    expenses_other_operation_1: float
    expenses_other_operation_2: float

    net_profit_1: float
    net_profit_2: float
    profit_income_tax_1: float
    profit_income_tax_2: float
    profit_after_income_tax_1: float
    profit_after_income_tax_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float

    name: str
    rank: str
