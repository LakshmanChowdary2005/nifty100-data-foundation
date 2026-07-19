from src.analytics.ratios import (
    pe_ratio,
    pb_ratio,
    earnings_yield,
    book_value_per_share,
    valuation_label,
)


def test_pe_ratio():
    assert pe_ratio(200, 10) == 20.0


def test_pe_ratio_zero():
    assert pe_ratio(200, 0) is None


def test_pb_ratio():
    assert pb_ratio(120, 40) == 3.0


def test_earnings_yield():
    assert earnings_yield(10, 200) == 5.0


def test_book_value_per_share():
    assert book_value_per_share(1000, 500, 100) == 15.0


def test_undervalued():
    assert valuation_label(10) == "Undervalued"


def test_fairly_valued():
    assert valuation_label(20) == "Fairly Valued"


def test_overvalued():
    assert valuation_label(40) == "Overvalued"