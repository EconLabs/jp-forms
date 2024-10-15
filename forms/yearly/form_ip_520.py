from sqlmodel import Field, SQLModel
from typing import Optional

class IP520Validator(SQLModel, table=True):
    """
    Schema for IP-520 Validator form

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
    closing_date: str
    branches: str
    start_year: int
    end_year: int

    incomes_interests_1: float
    incomes_interests_2: float
    incomes_personal_loans_1: float
    incomes_personal_loans_2: float
    incomes_mortage_loans_1: float
    incomes_mortage_loans_2: float
    incomes_other_1: float
    incomes_other_2: float
    incomes_rent_1: float
    incomes_rent_2: float
    incomes_dividends_1: float
    incomes_dividends_2: float
    incomes_financing_charges_1: float
    incomes_financing_charges_2: float
    incomes_service_charges_1: float
    incomes_service_charges_2: float
    incomes_commissions_1: float
    incomes_commissions_2: float
    incomes_finance_leasing_1: float
    incomes_finance_leasing_2: float
    incomes_capital_gain_loss_1: float
    incomes_capital_gain_loss_2: float
    incomes_other_operations_1: float
    incomes_other_operations_2: float
    incomes_total_1: float
    incomes_total_2: float

    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    interests_to_individuals_1: float
    interests_to_individuals_2: float
    interests_to_corporations_1: float
    interests_to_corporations_2: float
    corporation_936_1: float
    corporation_936_2: float
    other_corporation_1: float
    other_corporation_2: float
    interests_other_1: float
    interests_other_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_bad_debts_1: float
    expenses_bad_debts_2: float
    expenses_donations_1: float
    expenses_donations_2: float
    expenses_sales_taxes_1: float
    expenses_sales_taxes_2: float
    expenses_machinary_1: float
    expenses_machinary_2: float
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
    dividends_paid_1: float
    dividends_paid_2: float
    sales_tax_1: float
    sales_tax_2: float

    name: str
    rank: str

