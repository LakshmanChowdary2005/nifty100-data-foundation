import pandas as pd

try:
    # Read the Excel file
    df = pd.read_excel("data/market_cap.xlsx")

    print("=" * 50)
    print("Market Cap File Loaded Successfully")
    print("=" * 50)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nTotal Rows:")
    print(len(df))

    print("\nFirst 10 Rows:")
    print(df.head(10))

except FileNotFoundError:
    print("❌ market_cap.xlsx not found!")

except Exception as e:
    print(f"❌ Error: {e}")