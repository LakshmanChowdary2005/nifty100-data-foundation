from src.etl.normaliser import normalize_year
from src.etl.normaliser import normalize_ticker

print(normalize_year("2024"))
print(normalize_year("2024-25"))

print(normalize_ticker("tcs.ns"))
print(normalize_ticker("infy.bo"))
print(normalize_ticker(" Reliance.ns "))