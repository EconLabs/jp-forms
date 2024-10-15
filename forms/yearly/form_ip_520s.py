from sqlmodel import Field, SQLModel
from typing import Optional

class IP520sValidator(SQLModel, table=True):
    """
    Schema for IP-520s Validator form

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
    other_business_type: str
    risk_type: str
    branches: str
    branches_if_yes: str
    closing_date: str
    start_year: int
    end_year: int

    incomes_premium_earned_1: float
    incomes_premium_earned_2: float
    incomes_disability_1: float
    incomes_disability_2: float
    incomes_life_1: float
    incomes_life_2: float
    incomes_auto_1: float
    incomes_auto_2: float
    incomes_other_1: float
    incomes_other_2: float
    incomes_dividend_1: float
    incomes_dividend_2: float
    incomes_rent_1: float
    incomes_rent_2: float
    incomes_commissions_1: float
    incomes_commissions_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_capital_gain_loss_1: float
    incomes_capital_gain_loss_2: float
    incomes_other_operation_1: float
    incomes_other_operation_2: float
    incomes_total_1: float
    incomes_total_2: float

    expenses_1: float
    expenses_2: float
    expenses_premium_earned_1: float
    expenses_premium_earned_2: float
    expenses_disability_1: float
    expenses_disability_2: float
    expenses_life_1: float
    expenses_life_2: float
    expenses_auto_1: float
    expenses_auto_2: float
    expenses_other_1: float
    expenses_other_2: float
    expenses_increase_reserves_1: float
    expenses_increase_reserves_2: float
    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_commissions_1: float
    expenses_commissions_2: float
    expenses_to_employees_1: float
    expenses_to_employees_2: float
    expenses_independent_agents_1: float
    expenses_independent_agents_2: float
    expenses_interest_1: float
    expenses_interest_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_dividend_policy_holder_1: float
    expenses_dividend_policy_holder_2: float
    expenses_donation_1: float
    expenses_donation_2: float
    expenses_sales_tax_1: float
    expenses_sales_tax_2: float
    expenses_machinary_1: float
    expenses_machinary_2: float
    expenses_other_purchases_1: float
    expenses_other_purchases_2: float
    expenses_licenses_1: float
    expenses_licenses_2: float
    expenses_other_operating_1: float
    expenses_other_operating_2: float
    expenses_total_1: float
    expenses_total_2: float

    gross_profit_1: float
    gross_profit_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float

    name: str
    rank: str
