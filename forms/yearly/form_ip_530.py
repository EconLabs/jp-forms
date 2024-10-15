from sqlmodel import Field, SQLModel
from typing import Optional

class IP530Validator(SQLModel, table=True):
    """
    Schema for IP-530 Validator form
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
    other_business_type: str
    closing_date: str
    start_year: int
    end_year: int

    incomes_from_persons_1: float
    incomes_from_persons_2: float
    incomes_industries_businesses_1: float
    incomes_industries_businesses_2: float
    incomes_rent_1: float
    incomes_rent_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_comissions_1: float
    incomes_comissions_2: float
    incomes_gain_loss_1: float
    incomes_gain_loss_2: float
    incomes_operating_1: float
    incomes_operating_2: float

    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_donations_1: float
    expenses_donations_2: float
    expenses_sales_tax_1: float
    expenses_sales_tax_2: float
    expenses_machinary_equipment_1: float
    expenses_machinary_equipment_2: float
    expenses_other_purchases_1: float
    expenses_other_purchases_2: float
    expenses_licenses_1: float
    expenses_licenses_2: float
    expenses_other_operations_1: float
    expenses_other_operations_2: float
    expenses_total_1: float
    expenses_total_2: float

    gross_profit_1: float
    gross_profit_2: float
    profit_income_tax_1: float
    profit_income_tax_2: float
    profit_after_income_tax_1: float
    profit_after_income_tax_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float

    name: str
    rank: str
