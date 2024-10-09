from pydantic import BaseModel
from ..dao.db import DAO
import polars as pl

class IP480Validator(BaseModel):
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

# def IP_480(request):
#     if request.method == "POST":
#         # Retrieve form data
#         company_name = request.POST.get("company_name")
#         address = request.POST.get("address")
#         email = request.POST.get("email")
#         liaison_officer = request.POST.get("liaison_officer")
#         ssn = request.POST.get("ssn")
#         tel = request.POST.get("tel")
#         fax = request.POST.get("fax")
#         legal_form = request.POST.get("legal_form")
#         cfc = request.POST.get("cfc")
#         business_function = request.POST.get("business_function")
#         closing_date = request.POST.get("closing_date")
#         start_year = request.POST.get("start_year")
#         end_year = request.POST.get("end_year")
#         operation_incomes_1 = request.POST.get("operation_incomes_1")
#         operation_incomes_2 = request.POST.get("operation_incomes_2")
#         people_A_1 = request.POST.get("people_A_1")
#         people_A_2 = request.POST.get("people_A_2")
#         industries_businesses_A_1 = request.POST.get("industries_businesses_A_1")
#         industries_businesses_A_2 = request.POST.get("industries_businesses_A_2")
#         incomes_interests_1 = request.POST.get("incomes_interests_1")
#         incomes_interests_2 = request.POST.get("incomes_interests_2")
#         incomes_rents_1 = request.POST.get("incomes_rents_1")
#         incomes_rents_2 = request.POST.get("incomes_rents_2")
#         dividends_1 = request.POST.get("dividends_1")
#         dividends_2 = request.POST.get("dividends_2")
#         others_incomes_1 = request.POST.get("others_incomes_1")
#         others_incomes_2 = request.POST.get("others_incomes_2")
#         total_incomes_1 = request.POST.get("total_incomes_1")
#         total_incomes_2 = request.POST.get("total_incomes_2")
#         salaries_1 = request.POST.get("salaries_1")
#         salaries_2 = request.POST.get("salaries_2")
#         expenses_interests_1 = request.POST.get("expenses_interests_1")
#         expenses_interests_2 = request.POST.get("expenses_interests_2")
#         expenses_rents_1 = request.POST.get("expenses_rents_1")
#         expenses_rents_2 = request.POST.get("expenses_rents_2")
#         depreciation_1 = request.POST.get("depreciation_1")
#         depreciation_2 = request.POST.get("depreciation_2")
#         donations_1 = request.POST.get("donations_1")
#         donations_2 = request.POST.get("donations_2")
#         sales_tax_1 = request.POST.get("sales_tax_1")
#         sales_tax_2 = request.POST.get("sales_tax_2")
#         machinery_1 = request.POST.get("machinery_1")
#         machinery_2 = request.POST.get("machinery_2")
#         other_purchases_1 = request.POST.get("other_purchases_1")
#         other_purchases_2 = request.POST.get("other_purchases_2")
#         licenses_1 = request.POST.get("licenses_1")
#         licenses_2 = request.POST.get("licenses_2")
#         other_expenses_1 = request.POST.get("other_expenses_1")
#         other_expenses_2 = request.POST.get("other_expenses_2")
#         total_expenses_1 = request.POST.get("total_expenses_1")
#         total_expenses_2 = request.POST.get("total_expenses_2")
#         net_profit_1 = request.POST.get("net_profit_1")
#         net_profit_2 = request.POST.get("net_profit_2")
#         income_tax_1 = request.POST.get("income_tax_1")
#         income_tax_2 = request.POST.get("income_tax_2")
#         profit_after_tax_1 = request.POST.get("profit_after_tax_1")
#         profit_after_tax_2 = request.POST.get("profit_after_tax_2")
#         withheld_tax_1 = request.POST.get("withheld_tax_1")
#         withheld_tax_2 = request.POST.get("withheld_tax_2")
#         signature = request.POST.get("signature")
#         rank = request.POST.get("rank")

#         data = [
#             pl.Series("company_name", [company_name], dtype=pl.String),
#             pl.Series("address", [address], dtype=pl.String),
#             pl.Series("email", [email], dtype=pl.String),
#             pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),
#             pl.Series("ssn", [ssn], dtype=pl.String),
#             pl.Series("tel", [tel], dtype=pl.String),
#             pl.Series("fax", [fax], dtype=pl.String),
#             pl.Series("legal_form", [legal_form], dtype=pl.String),
#             pl.Series("cfc", [cfc], dtype=pl.String),
#             pl.Series("business_function", [business_function], dtype=pl.String),
#             pl.Series("closing_date", [closing_date], dtype=pl.String),
#             pl.Series("start_year", [start_year], dtype=pl.String),
#             pl.Series("end_year", [end_year], dtype=pl.String),
#             pl.Series("operation_incomes_1", [float(operation_incomes_1)], dtype=pl.Float64),
#             pl.Series("operation_incomes_2", [float(operation_incomes_2)], dtype=pl.Float64),
#             pl.Series("people_A_1", [float(people_A_1)], dtype=pl.Float64),
#             pl.Series("people_A_2", [float(people_A_2)], dtype=pl.Float64),
#             pl.Series("industries_businesses_A_1", [float(industries_businesses_A_1)], dtype=pl.Float64),
#             pl.Series("industries_businesses_A_2", [float(industries_businesses_A_2)], dtype=pl.Float64),
#             pl.Series("incomes_interests_1", [float(incomes_interests_1)], dtype=pl.Float64),
#             pl.Series("incomes_interests_2", [float(incomes_interests_2)], dtype=pl.Float64),
#             pl.Series("incomes_rents_1", [float(incomes_rents_1)], dtype=pl.Float64),
#             pl.Series("incomes_rents_2", [float(incomes_rents_2)], dtype=pl.Float64),
#             pl.Series("dividends_1", [float(dividends_1)], dtype=pl.Float64),
#             pl.Series("dividends_2", [float(dividends_2)], dtype=pl.Float64),
#             pl.Series("others_incomes_1", [float(others_incomes_1)], dtype=pl.Float64),
#             pl.Series("others_incomes_2", [float(others_incomes_2)], dtype=pl.Float64),
#             pl.Series("total_incomes_1", [float(total_incomes_1)], dtype=pl.Float64),
#             pl.Series("total_incomes_2", [float(total_incomes_2)], dtype=pl.Float64),
#             pl.Series("salaries_1", [float(salaries_1)], dtype=pl.Float64),
#             pl.Series("salaries_2", [float(salaries_2)], dtype=pl.Float64),
#             pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
#             pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
#             pl.Series("expenses_rents_1", [float(expenses_rents_1)], dtype=pl.Float64),
#             pl.Series("expenses_rents_2", [float(expenses_rents_2)], dtype=pl.Float64),
#             pl.Series("depreciation_1", [float(depreciation_1)], dtype=pl.Float64),
#             pl.Series("depreciation_2", [float(depreciation_2)], dtype=pl.Float64),
#             pl.Series("donations_1", [float(donations_1)], dtype=pl.Float64),
#             pl.Series("donations_2", [float(donations_2)], dtype=pl.Float64),
#             pl.Series("sales_tax_1", [float(sales_tax_1)], dtype=pl.Float64),
#             pl.Series("sales_tax_2", [float(sales_tax_2)], dtype=pl.Float64),
#             pl.Series("machinery_1", [float(machinery_1)], dtype=pl.Float64),
#             pl.Series("machinery_2", [float(machinery_2)], dtype=pl.Float64),
#             pl.Series("other_purchases_1", [float(other_purchases_1)], dtype=pl.Float64),
#             pl.Series("other_purchases_2", [float(other_purchases_2)], dtype=pl.Float64),
#             pl.Series("licenses_1", [float(licenses_1)], dtype=pl.Float64),
#             pl.Series("licenses_2", [float(licenses_2)], dtype=pl.Float64),
#             pl.Series("other_expenses_1", [float(other_expenses_1)], dtype=pl.Float64),
#             pl.Series("other_expenses_2", [float(other_expenses_2)], dtype=pl.Float64),
#             pl.Series("total_expenses_1", [float(total_expenses_1)], dtype=pl.Float64),
#             pl.Series("total_expenses_2", [float(total_expenses_2)], dtype=pl.Float64),
#             pl.Series("net_profit_1", [float(net_profit_1)], dtype=pl.Float64),
#             pl.Series("net_profit_2", [float(net_profit_2)], dtype=pl.Float64),
#             pl.Series("income_tax_1", [float(income_tax_1)], dtype=pl.Float64),
#             pl.Series("income_tax_2", [float(income_tax_2)], dtype=pl.Float64),
#             pl.Series("profit_after_tax_1", [float(profit_after_tax_1)], dtype=pl.Float64),
#             pl.Series("profit_after_tax_2", [float(profit_after_tax_2)], dtype=pl.Float64),
#             pl.Series("withheld_tax_1", [float(withheld_tax_1)], dtype=pl.Float64),
#             pl.Series("withheld_tax_2", [float(withheld_tax_2)], dtype=pl.Float64),
#             pl.Series("signature", [signature], dtype=pl.String),
#             pl.Series("rank", [rank], dtype=pl.String),
#         ]
        
#         df = pl.DataFrame(data)
#         DAO().insert_forms(df, "IP_480", 27)

#         return render(request, "forms/succesfull.html")
#     return render(request, "forms/yearly/ingreso_neto/IP-480.html")

class IP_480FormView():
    def __init__(self, form: IP480Validator):
        self.raw = form
        self.df = []
        
    def insert_to_db(self):
        for key, value in self.raw:
            self.df.append(pl.Series(key, [value]))
            
        df = pl.DataFrame(self.df)
        DAO().insert_forms(df, "IP_4480", 15)
