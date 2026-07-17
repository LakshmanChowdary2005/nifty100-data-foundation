from src.analytics.ratios import *


def test_net_profit_margin():
    assert net_profit_margin(200, 1000) == 20


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(200, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(300, 1000) == 30


def test_opm_check():
    assert check_opm(30, 28) is True


def test_roe():
    assert return_on_equity(100, 400, 100) == 20


def test_negative_equity():
    assert return_on_equity(100, -300, 100) is None


def test_roce():
    assert return_on_capital_employed(200, 400, 100, 500) == 20


def test_roa():
    assert return_on_assets(100, 2000) == 5