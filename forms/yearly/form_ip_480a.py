from pydantic import BaseModel
from ..dao.db import DAO
import polars as pl

class IP480aValidator(BaseModel):
    company_name: str
    address: str
    email: str
    liaison_officer: str
    ssn: str
    tel: str
    fax: str
    business_function: str
    legal_form: str
    cfc: str
    closing_date: str
    start_year: int
    end_year: int
    
    people_A_1: float
    people_A_2: float
    industries_businesses_A_1: float
    industries_businesses_A_2: float
    passenger_fares_1: float
    passenger_fares_2: float
    freight_1: float
    freight_2: float
    ship_USA_1: float
    ship_USA_2: float
    ship_VIRGISLND_1: float
    ship_VIRGISLND_2: float
    SHIP_fORECNTY_1: float
    SHIP_fORECNTY_2: float
    income_interest_1: float
    income_interest_2: float
    income_rent_1: float
    income_rent_2: float
    commissions_1: float
    commissions_2: float
    capital_gain_loss_1: float
    capital_gain_loss_2: float
    other_incomes_1: float
    other_incomes_2: float
    total_incomes_1: float
    total_incomes_2: float
    
    salaries_1: float
    salaries_2: float
    commissions_employees_1: float
    commissions_employees_2: float
    commissions_independent_1: float
    commissions_independent_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rents_1: float
    expenses_rents_2: float
    depreciation_1: float
    depreciation_2: float
    bad_debts_1: float
    bad_debts_2: float
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

class IP_480aFormView():
    def __init__(self, form: IP480aValidator):
        self.raw = form
        self.df = []
        
    def insert_to_db(self):
        for key, value in self.raw:
            self.df.append(pl.Series(key, [value]))
            
        df = pl.DataFrame(self.df)
        DAO().insert_forms(df, "IP_480a", 34)