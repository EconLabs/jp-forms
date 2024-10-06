from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class IP110Yearly(SQLModel, table=True):
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
    branches: str
    closing_date: str
    start_year: int
    end_year: int
    incomes_services_revenues_1: float
    incomes_services_revenues_2: float
    incomes_industries_1: float
    incomes_industries_2: float
    incomes_persons_1: float
    incomes_persons_2: float
    incomes_sale_merchandise_1: float
    incomes_sale_merchandise_2: float
    incomes_rents_1: float
    incomes_rents_2: float
    incomes_interests_1: float
    incomes_interests_2: float
    incomes_capital_gain_loss_1: float
    incomes_capital_gain_loss_2: float
    others_incomes_1: float
    others_incomes_2: float
    total_income_1: float
    total_income_2: float
    expenses_1: float
    expenses_2: float
    expenses_salaries_wages_bonus_1: float
    expenses_salaries_wages_bonus_2: float
    expenses_interests_1: float
    expenses_interests_2: float
    expenses_rents_1: float
    expenses_rents_2: float
    expenses_depreciation_1: float
    expenses_depreciation_2: float
    expenses_bad_debts_1: float
    expenses_bad_debts_2: float
    expenses_donation_1: float
    expenses_donation_2: float
    expenses_sales_tax_1: float
    expenses_sales_tax_2: float
    expenses_machinery_1: float
    expenses_machinery_2: float
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
    net_profit_income_tax_1: float
    net_profit_income_tax_2: float
    profit_after_tax_1: float
    profit_after_tax_2: float
    withheld_tax_1: float
    withheld_tax_2: float
    signature: str
    rank: str


if __name__ == "__main__":
    engine = create_engine("sqlite:///db.sqlite")
    SQLModel.metadata.create_all(engine)

    form = IP110Yearly(
        company_name="John Doe1",
        address="123 Main Street",
        email="name@test.com",
        liaison_officer="John Doe2",
        ssn="123456789",
        tel="123456789",
        fax="123456789",
        legal_form="John Doe3",
        cfc="John Doe4",
        business_type="John Doe5",
        business_function="John Doe6",
        branches="John Doe7",
        closing_date="John Doe8",
        start_year=2021,
        end_year=2023,
        incomes_services_revenues_1=1.0,
        incomes_services_revenues_2=1.0,
        incomes_industries_1=1.0,
        incomes_industries_2=1.0,
        incomes_persons_1=1.0,
        incomes_persons_2=1.0,
        incomes_sale_merchandise_1=1.0,
        incomes_sale_merchandise_2=1.0,
        incomes_rents_1=1.0,
        incomes_rents_2=1.0,
        incomes_interests_1=1.0,
        incomes_interests_2=1.0,
        incomes_capital_gain_loss_1=1.0,
        incomes_capital_gain_loss_2=1.0,
        others_incomes_1=1.0,
        others_incomes_2=1.0,
        total_income_1=1.0,
        total_income_2=1.0,
        expenses_1=1.0,
        expenses_2=1.0,
        expenses_salaries_wages_bonus_1=1.0,
        expenses_salaries_wages_bonus_2=1.0,
        expenses_interests_1=1.0,
        expenses_interests_2=1.0,
        expenses_rents_1=1.0,
        expenses_rents_2=1.0,
        expenses_depreciation_1=1.0,
        expenses_depreciation_2=1.0,
        expenses_bad_debts_1=1.0,
        expenses_bad_debts_2=1.0,
        expenses_donation_1=1.0,
        expenses_donation_2=1.0,
        expenses_sales_tax_1=1.0,
        expenses_sales_tax_2=1.0,
        expenses_machinery_1=1.0,
        expenses_machinery_2=1.0,
        other_purchases_1=1.0,
        other_purchases_2=1.0,
        licenses_1=1.0,
        licenses_2=1.0,
        other_expenses_1=1.0,
        other_expenses_2=1.0,
        total_expenses_1=1.0,
        total_expenses_2=1.0,
        net_profit_1=1.0,
        net_profit_2=1.0,
        net_profit_income_tax_1=1.0,
        net_profit_income_tax_2=1.0,
        profit_after_tax_1=1.0,
        profit_after_tax_2=1.0,
        withheld_tax_1=1.0,
        withheld_tax_2=1.0,
        signature="John Doe11",
        rank="John Doe12",
    )

    with Session(engine) as session:
        session.add(form)
        session.commit()
