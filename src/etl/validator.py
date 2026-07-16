import pandas as pd
from pathlib import Path

# -------------------------------
# Folder Paths
# -------------------------------
DATA_FOLDER = Path("data/processed")
OUTPUT_FOLDER = Path("output")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# -------------------------------
# Read Excel Files
# -------------------------------
companies = pd.read_excel(DATA_FOLDER / "companies.xlsx")
profit = pd.read_excel(DATA_FOLDER / "profitandloss.xlsx")
balance = pd.read_excel(DATA_FOLDER / "balancesheet.xlsx")
cashflow = pd.read_excel(DATA_FOLDER / "cashflow.xlsx")

# -------------------------------
# Validation List
# -------------------------------
failures = []

# ==================================================
# DQ-01 : company_id must be unique
# ==================================================

duplicates = companies[companies.duplicated("company_id")]

for _, row in duplicates.iterrows():
    failures.append([
        "DQ-01",
        "companies",
        row["company_id"],
        "Duplicate company_id",
        "CRITICAL"
    ])

# ==================================================
# DQ-02 : (company_id, year) must be unique
# ==================================================

duplicates = profit[profit.duplicated(["company_id", "year"])]

for _, row in duplicates.iterrows():
    failures.append([
        "DQ-02",
        "profitandloss",
        row["company_id"],
        "Duplicate company_id + year",
        "CRITICAL"
    ])

# ==================================================
# DQ-03 : Foreign Key Validation
# ==================================================

company_ids = set(companies["company_id"])

for _, row in profit.iterrows():

    if row["company_id"] not in company_ids:

        failures.append([
            "DQ-03",
            "profitandloss",
            row["company_id"],
            "Company ID not found",
            "CRITICAL"
        ])

# ==================================================
# DQ-04 : Sales must be positive
# ==================================================

negative_sales = profit[profit["sales"] <= 0]

for _, row in negative_sales.iterrows():

    failures.append([
        "DQ-04",
        "profitandloss",
        row["company_id"],
        "Sales <= 0",
        "WARNING"
    ])

# ==================================================
# DQ-05 : Balance Sheet Validation
# Assets ≈ Liabilities + Equity
# ==================================================

for _, row in balance.iterrows():

    assets = row["assets"]
    liabilities = row["liabilities"]
    equity = row["equity"]

    difference = abs(assets - (liabilities + equity))

    if difference > 100:

        failures.append([
            "DQ-05",
            "balancesheet",
            row["company_id"],
            "Assets != Liabilities + Equity",
            "WARNING"
        ])

# ==================================================
# Create Report
# ==================================================

report = pd.DataFrame(
    failures,
    columns=[
        "Rule",
        "Table",
        "Company_ID",
        "Issue",
        "Severity"
    ]
)

report.to_csv(
    OUTPUT_FOLDER / "validation_failures.csv",
    index=False
)

# ==================================================
# Summary
# ==================================================

print("\n" + "=" * 50)
print("VALIDATION REPORT")
print("=" * 50)

print(f"Companies               : {len(companies)}")
print(f"Profit Records          : {len(profit)}")
print(f"Balance Sheet Records   : {len(balance)}")
print(f"Cash Flow Records       : {len(cashflow)}")

print("-" * 50)

print(f"Total Validation Issues : {len(report)}")

critical = len(report[report["Severity"] == "CRITICAL"])
warning = len(report[report["Severity"] == "WARNING"])

print(f"Critical Issues         : {critical}")
print(f"Warning Issues          : {warning}")

print("-" * 50)

print("Validation Report Saved:")
print(OUTPUT_FOLDER / "validation_failures.csv")

print("=" * 50)