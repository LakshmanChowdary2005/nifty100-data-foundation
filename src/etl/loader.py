import pandas as pd
from pathlib import Path

# Folder paths
RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")

# Create processed folder
PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)

# Find all Excel files
excel_files = list(RAW_FOLDER.glob("*.xlsx"))

print(f"\nFound {len(excel_files)} Excel files\n")

# Read each Excel file
for file in excel_files:

    print("=" * 60)
    print("Reading:", file.name)

    df = pd.read_excel(file, engine="openpyxl")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nFirst 5 Rows:")
    print(df.head())

    # Save a copy
    output_file = PROCESSED_FOLDER / file.name
    df.to_excel(output_file, index=False)

    print(f"\nSaved: {output_file}")

print("\nAll Excel files loaded successfully.")