from src.analytics.ratios import (
    current_ratio,
    quick_ratio,
    cash_ratio,
    working_capital,
    liquidity_label,
)


def test_current_ratio():
    assert current_ratio(200, 100) == 2.0


def test_current_ratio_zero():
    assert current_ratio(200, 0) is None


def test_quick_ratio():
    assert quick_ratio(200, 50, 100) == 1.5


def test_cash_ratio():
    assert cash_ratio(80, 100) == 0.8


def test_working_capital():
    assert working_capital(250, 100) == 150


def test_liquidity_strong():
    assert liquidity_label(2.5) == "Strong"


def test_liquidity_average():
    assert liquidity_label(1.2) == "Average"


def test_liquidity_weak():
    assert liquidity_label(0.8) == "Weak"