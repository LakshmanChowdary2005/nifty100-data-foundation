from src.analytics.ratios import (
    earnings_per_share,
    price_to_earnings,
    book_value_per_share,
    price_to_book,
    price_to_sales,
    valuation_label,
)


def test_eps():
    assert earnings_per_share(1000, 100) == 10.0


def test_eps_zero():
    assert earnings_per_share(1000, 0) is None


def test_pe_ratio():
    assert price_to_earnings(200, 10) == 20.0


def test_book_value():
    assert book_value_per_share(5000, 100) == 50.0


def test_price_to_book():
    assert price_to_book(100, 50) == 2.0


def test_price_to_sales():
    assert price_to_sales(10000, 5000) == 2.0


def test_undervalued():
    assert valuation_label(12) == "Undervalued"


def test_fairly_valued():
    assert valuation_label(20) == "Fairly Valued"


def test_overvalued():
    assert valuation_label(35) == "Overvalued"