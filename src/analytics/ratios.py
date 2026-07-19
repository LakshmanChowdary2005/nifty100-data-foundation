"""
Profitability Ratio Functions
Sprint 2 - Day 08
"""

def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None

    return (operating_profit / sales) * 100


def check_opm(calculated_opm, source_opm):
    """
    Compare calculated OPM with source OPM.
    Returns True if difference is greater than 1%.
    """
    if calculated_opm is None or source_opm is None:
        return False

    difference = abs(calculated_opm - source_opm)

    return difference > 1


def return_on_equity(net_profit, equity, reserves):
    """
    ROE = Net Profit / (Equity + Reserves) * 100
    """

    total_equity = equity + reserves

    if total_equity <= 0:
        return None

    return (net_profit / total_equity) * 100


def return_on_capital_employed(ebit, equity, reserves, borrowings):
    """
    ROCE = EBIT / (Equity + Reserves + Borrowings) * 100
    """

    capital = equity + reserves + borrowings

    if capital <= 0:
        return None

    return (ebit / capital) * 100


def return_on_assets(net_profit, total_assets):
    """
    ROA = Net Profit / Total Assets * 100
    """

    if total_assets == 0:
        return None

    return (net_profit / total_assets) * 100
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