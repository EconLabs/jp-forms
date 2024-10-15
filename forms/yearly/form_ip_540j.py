from sqlmodel import Field, SQLModel
from typing import Optional

class IP540JValidator(SQLModel, table=True):
    """
    Schema for IP-540J Validator form
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
    incomes_industries_business_1: float
    incomes_industries_business_2: float
    expenses_newspapers_1: float
    expenses_newspapers_2: float
    expenses_radio_television_1: float
    expenses_radio_television_2: float
    expenses_other_1: float
    expenses_other_2: float
    gross_profit_1: float
    gross_profit_2: float
    dividends_paid_1: float
    dividends_paid_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_gain_loss_1: float
    expenses_gain_loss_2: float
    dividends_paid_other_1: float
    dividends_paid_other_2: float
    incomes_total_1: float
    incomes_total_2: float
    expenses_total_1: float
    expenses_total_2: float
    salaries_wages_bonus_1: float
    salaries_wages_bonus_2: float
    interests_1: float
    interests_2: float
    rents_1: float
    rents_2: float
    depreciation_1: float
    depreciation_2: float
    other_taxes_1: float
    other_taxes_2: float
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
    other_operating_expenses_1: float
    other_operating_expenses_2: float
    profit_incomes_tax_1: float
    profit_incomes_tax_2: float
    profit_incomes_mortage_loans_1: float
    profit_incomes_mortage_loans_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float

    name: str
    rank: str
