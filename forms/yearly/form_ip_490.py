from pydantic import BaseModel
from ..dao.db import DAO
import polars as pl

class IP490Validator(BaseModel):
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
    
    # Financial fields for the first and second periods
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
    
    # Other fields
    name: str
    rank: str

class IP_490FormView():
    def __init__(self, form: IP490Validator):
        self.raw = form
        self.df = []
        
    def insert_to_db(self):
        for key, value in self.raw:
            self.df.append(pl.Series(key, [value]))
        
        df = pl.DataFrame(self.df)
        DAO().insert_forms(df, "IP_490", 35)