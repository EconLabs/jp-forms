from sqlmodel import Field, SQLModel
from typing import Optional

class IP510Validator(SQLModel, table=True):
    """
    Schema for IP-510 Validator form

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
    accounting_period: str
    main_product_1: str
    main_product_2: str
    raw_material_used: str
    closing_date: str
    start_year: int
    end_year: int


    sales_from_persons_1: float
    sales_from_persons_2: float
    sales_industries_businesses_1: float
    sales_industries_businesses_2: float
    sales_goods_1: float
    sales_goods_2: float
    sales_exports_goods_1: float
    sales_exports_goods_2: float
    sales_goods_from_others_firms_1: float
    sales_goods_from_others_firms_2: float
    sales_exports_goods_other_firms_1: float
    sales_exports_goods_other_firms_2: float
    total_cost_1: float
    total_cost_2: float
    total_cost_inventories_begginning_1: float
    total_cost_inventories_begginning_2: float
    total_cost_purchases_1: float
    total_cost_purchases_2: float
    total_cost_total_raw_1: float
    total_cost_total_raw_2: float
    total_cost_imported_1: float
    total_cost_imported_2: float
    total_cost_others_1: float
    total_cost_others_2: float
    total_cost_direct_wages_1: float
    total_cost_direct_wages_2: float
    total_cost_depreciation_1: float
    total_cost_depreciation_2: float
    total_cost_rent_land_1: float
    total_cost_rent_land_2: float
    total_cost_other_direct_1: float
    total_cost_other_direct_2: float
    total_cost_indirect_cost_1: float
    total_cost_indirect_cost_2: float
    total_cost_inventories_end_1: float
    total_cost_inventories_end_2: float
    gross_profit_1: float
    gross_profit_2: float
    other_operating_1: float
    other_operating_2: float
    other_operating_interest_1: float
    other_operating_interest_2: float
    other_operating_rent_land_1: float
    other_operating_rent_land_2: float
    other_operating_capital_gain_1: float
    other_operating_capital_gain_2: float
    other_operating_other_1: float
    other_operating_other_2: float
    total_gross_1: float
    total_gross_2: float

    # Expenses not included
    expenses_not_included_1: float
    expenses_not_included_2: float
    expenses_not_included_salaries_1: float
    expenses_not_included_salaries_2: float
    expenses_not_included_interest_1: float
    expenses_not_included_interest_2: float
    expenses_not_included_depreciation_1: float
    expenses_not_included_depreciation_2: float
    expenses_not_included_donations_1: float
    expenses_not_included_donations_2: float
    expenses_not_included_rent_land_1: float
    expenses_not_included_rent_land_2: float
    expenses_not_included_other_operating_1: float
    expenses_not_included_other_operating_2: float
    expenses_not_included_sales_tax_1: float
    expenses_not_included_sales_tax_2: float
    expenses_not_included_machinery_1: float
    expenses_not_included_machinery_2: float
    expenses_not_included_on_other_1: float
    expenses_not_included_on_other_2: float
    expenses_not_included_licenses_1: float
    expenses_not_included_licenses_2: float

    net_profit_loss_1: float
    net_profit_loss_2: float
    net_profit_loss_income_tax_1: float
    net_profit_loss_income_tax_2: float
    profit_after_tax_1: float
    profit_after_tax_2: float
    sales_and_use_withheld_1: float
    sales_and_use_withheld_2: float

    branches: str
    branches_if_yes: str
    name: str
    rank: str

