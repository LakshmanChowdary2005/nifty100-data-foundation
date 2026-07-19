from src.analytics.ratios import (
    price_to_earnings,
    price_to_book,
    earnings_yield,
    book_value_per_share,
    valuation_label,
)


def test_price_to_earnings():
    assert price_to_earnings(200, 20) == 10.0


def test_price_to_earnings_zero():
    assert price_to_earnings(200, 0) is None


def test_price_to_book():
    assert price_to_book(300, 100) == 3.0


def test_earnings_yield():
    assert earnings_yield(20, 200) == 10.0


def test_book_value_per_share():
    assert book_value_per_share(1000, 500, 100) == 15.0


def test_undervalued():
    assert valuation_label(12) == "Undervalued"


def test_fairly_valued():
    assert valuation_label(20) == "Fairly Valued"


def test_overvalued():
    assert valuation_label(45) == "Overvalued"