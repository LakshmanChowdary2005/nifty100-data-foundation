def debt_to_equity(borrowings, equity, reserves):
    total_equity = equity + reserves

    if total_equity <= 0:
        return None

    return round(borrowings / total_equity, 2)


def high_leverage_flag(de_ratio):
    if de_ratio is None:
        return False

    return de_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    if interest == 0:
        return None

    return round((operating_profit + other_income) / interest, 2)


def interest_warning(icr):
    if icr is None:
        return False

    return icr < 2


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None

    return round(sales / total_assets, 2)
