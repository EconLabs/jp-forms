from pydantic import BaseModel
from ..dao.db import DAO
import polars as pl

class IP520aValidator(BaseModel):
    company_name: str
    address: str
    email: str
    liaison_officer: str
    ssn: str
    tel: str
    fax: str
    legal_form: str
    cfc: str
    start_month: str
    start_year: int
    end_year: int

    # Income fields for the first and second periods
    incomes_services_fee_1: float
    incomes_services_fee_2: float
    incomes_comissions_1: float
    incomes_comissions_2: float
    incomes_rent_1: float
    incomes_rent_2: float
    incomes_interest_1: float
    incomes_interest_2: float
    incomes_capital_gain_loss_1: float
    incomes_capital_gain_loss_2: float
    incomes_other_operating_1: float
    incomes_other_operating_2: float
    incomes_total_1: float
    incomes_total_2: float
    
    # Expenses fields for the first and second periods
    expenses_1: float
    expenses_2: float
    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_commissions_1: float
    expenses_commissions_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rent_1: float
    expenses_rent_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
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
    expenses_other_operation_1: float
    expenses_other_operation_2: float
    expenses_total_1: float
    expenses_total_2: float
    
    # Profit and tax-related fields
    net_profit_loss_1: float
    net_profit_loss_2: float
    sales_tax_withheld_1: float
    sales_tax_withheld_2: float
    percent_local_enterprises: float
    percent_foreign_enterprises: float
    
    # Other fields
    name: str
    rank: str

class IP_520aFormView():
    def __init__(self, form: IP520aValidator):
        self.raw = form
        self.df = []
        
    def insert_to_db(self):
        for key, value in self.raw:
            self.df.append(pl.Series(key, [value]))
        
        df = pl.DataFrame(self.df)
        DAO().insert_forms(df, "IP_520a", 38)
