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