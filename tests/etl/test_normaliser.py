from src.etl.normaliser import normalize_year, normalize_ticker

def test_year_1():
    assert normalize_year("2024") == 2024

def test_year_2():
    assert normalize_year("2024-25") == 2024

def test_year_3():
    assert normalize_year(2023) == 2023

def test_ticker_1():
    assert normalize_ticker("tcs.ns") == "TCS"

def test_ticker_2():
    assert normalize_ticker("infy.bo") == "INFY"

def test_ticker_3():
    assert normalize_ticker(" Reliance.ns ") == "RELIANCE"