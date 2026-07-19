from src.analytics.ratios import (
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    interest_warning,
    net_debt,
    asset_turnover,
)


def test_debt_to_equity():
    assert debt_to_equity(100, 300, 200) == 0.2


def test_zero_equity():
    assert debt_to_equity(100, 0, 0) is None


def test_high_leverage():
    assert high_leverage_flag(6) is True


def test_normal_leverage():
    assert high_leverage_flag(1.5) is False


def test_interest_coverage():
    assert interest_coverage_ratio(500, 100, 200) == 3.0


def test_interest_warning():
    assert interest_warning(1.5) is True


def test_net_debt():
    assert net_debt(500, 100) == 400


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2.0