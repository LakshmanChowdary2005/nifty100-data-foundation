"""
Financial Ratio Functions
Sprint 2 - Days 08, 09 and 10
"""

# =========================
# DAY 08
# =========================

def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return round((operating_profit / sales) * 100, 2)


def check_opm(calculated_opm, source_opm):
    if calculated_opm is None or source_opm is None:
        return False
    return abs(calculated_opm - source_opm) > 1


def return_on_equity(net_profit, equity, reserves):
    total_equity = equity + reserves
    if total_equity <= 0:
        return None
    return round((net_profit / total_equity) * 100, 2)


def return_on_capital_employed(ebit, equity, reserves, borrowings):
    capital = equity + reserves + borrowings
    if capital <= 0:
        return None
    return round((ebit / capital) * 100, 2)


def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return round((net_profit / total_assets) * 100, 2)


# =========================
# DAY 09
# =========================

def debt_to_equity(borrowings, equity, reserves):
    total_equity = equity + reserves
    if total_equity <= 0:
        return None
    return round(borrowings / total_equity, 2)


def high_leverage_flag(de_ratio):
    return de_ratio is not None and de_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    if interest == 0:
        return None
    return round((operating_profit + other_income) / interest, 2)


def interest_warning(icr):
    return icr is not None and icr < 2


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return round(sales / total_assets, 2)


# =========================
# DAY 10
# =========================

def revenue_growth(current_sales, previous_sales):
    if previous_sales == 0:
        return None
    return round(((current_sales - previous_sales) / previous_sales) * 100, 2)


def profit_growth(current_profit, previous_profit):
    if previous_profit == 0:
        return None
    return round(((current_profit - previous_profit) / previous_profit) * 100, 2)


def eps_growth(current_eps, previous_eps):
    if previous_eps == 0:
        return None
    return round(((current_eps - previous_eps) / previous_eps) * 100, 2)


def cagr(beginning_value, ending_value, years):
    if beginning_value <= 0 or years <= 0:
        return None
    return round((((ending_value / beginning_value) ** (1 / years)) - 1) * 100, 2)


def growth_label(growth):
    if growth is None:
        return "Unknown"
    if growth >= 20:
        return "High Growth"
    if growth >= 10:
        return "Moderate Growth"
    return "Low Growth"
def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None
    return round(sales / total_assets, 2)
def current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return None
    return round(current_assets / current_liabilities, 2)


def quick_ratio(current_assets, inventory, current_liabilities):
    if current_liabilities == 0:
        return None
    return round((current_assets - inventory) / current_liabilities, 2)


def cash_ratio(cash, current_liabilities):
    if current_liabilities == 0:
        return None
    return round(cash / current_liabilities, 2)


def working_capital(current_assets, current_liabilities):
    return current_assets - current_liabilities


def liquidity_label(current_ratio_value):
    if current_ratio_value is None:
        return "Unknown"

    if current_ratio_value >= 2:
        return "Strong"

    if current_ratio_value >= 1:
        return "Average"

    return "Weak"