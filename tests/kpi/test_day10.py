from src.analytics.ratios import (
    revenue_growth,
    profit_growth,
    eps_growth,
    cagr,
    growth_label,
)


def test_revenue_growth():
    assert revenue_growth(1200, 1000) == 20.0


def test_revenue_growth_zero():
    assert revenue_growth(1200, 0) is None


def test_profit_growth():
    assert profit_growth(150, 100) == 50.0


def test_eps_growth():
    assert eps_growth(6, 5) == 20.0


def test_cagr():
    assert cagr(100, 121, 2) == 10.0


def test_high_growth():
    assert growth_label(25) == "High Growth"


def test_moderate_growth():
    assert growth_label(15) == "Moderate Growth"


def test_low_growth():
    assert growth_label(5) == "Low Growth"