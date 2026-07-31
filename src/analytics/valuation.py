import sqlite3
import pandas as pd
import os

# -----------------------------
# Create output folder
# -----------------------------
os.makedirs("output", exist_ok=True)

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql(
    "SELECT * FROM companies",
    conn
)

ratios = pd.read_sql(
    "SELECT * FROM financial_ratios",
    conn
)

cashflow = pd.read_sql(
    "SELECT * FROM cashflow",
    conn
)

conn.close()

# -----------------------------
# Read Market Cap
# -----------------------------
market = pd.read_excel("data/market_cap.xlsx")

# -----------------------------
# Latest Cash Flow
# -----------------------------
cash_latest = (
    cashflow
    .sort_values("year")
    .groupby("company_id")
    .tail(1)
)

cash_latest = cash_latest[
    [
        "company_id",
        "operating_cf"
    ]
]

# -----------------------------
# Merge Data
# -----------------------------
valuation = (
    companies
    .merge(ratios, on="company_id")
    .merge(cash_latest, on="company_id")
    .merge(
        market[
            [
                "company_id",
                "market_cap_crore"
            ]
        ],
        on="company_id"
    )
)

# -----------------------------
# FCF Yield
# -----------------------------
valuation["FCF_yield_pct"] = (
    valuation["operating_cf"]
    / valuation["market_cap_crore"]
) * 100

# -----------------------------
# Sector Median PE
# -----------------------------
sector_pe = (
    valuation
    .groupby("sector")["pe_ratio"]
    .median()
)

valuation["sector_median_pe"] = valuation["sector"].map(
    sector_pe
)

# -----------------------------
# PE vs Sector Median
# -----------------------------
valuation["PE_vs_sector_pct"] = (
    valuation["pe_ratio"]
    / valuation["sector_median_pe"]
) * 100

# -----------------------------
# Flag Companies
# -----------------------------
def get_flag(row):

    if row["pe_ratio"] > row["sector_median_pe"] * 1.5:
        return "Caution"

    elif row["pe_ratio"] < row["sector_median_pe"] * 0.7:
        return "Discount"

    return "Fair"


valuation["flag"] = valuation.apply(
    get_flag,
    axis=1
)

# -----------------------------
# Rename Columns
# -----------------------------
valuation.rename(
    columns={
        "pe_ratio": "PE"
    },
    inplace=True
)

# -----------------------------
# Create Missing Sprint Columns
# -----------------------------
valuation["PB"] = 0
valuation["EV_EBITDA"] = 0
valuation["Median_5Y_PE"] = valuation["sector_median_pe"]

# -----------------------------
# Final Output
# -----------------------------
summary = valuation[
    [
        "company_id",
        "company_name",
        "sector",
        "PE",
        "PB",
        "EV_EBITDA",
        "FCF_yield_pct",
        "Median_5Y_PE",
        "PE_vs_sector_pct",
        "flag",
    ]
]

summary.to_excel(
    "output/valuation_summary.xlsx",
    index=False
)

summary[
    summary["flag"] != "Fair"
].to_csv(
    "output/valuation_flags.csv",
    index=False
)

print("=" * 50)
print("VALUATION COMPLETED")
print("=" * 50)
print("Companies :", len(summary))
print("Summary   : output/valuation_summary.xlsx")
print("Flags     : output/valuation_flags.csv")