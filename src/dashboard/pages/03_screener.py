import streamlit as st
from utils.db import get_companies, get_financial_ratios

st.set_page_config(page_title="Stock Screener", layout="wide")

st.title("🔍 Stock Screener")

# Load Data
companies = get_companies()
ratios = get_financial_ratios()

# Merge company details with ratios
df = companies.merge(ratios, on="company_id")

st.sidebar.header("Filters")

# Search Box
search = st.sidebar.text_input("Search Company")

# Sliders
min_roe = st.sidebar.slider(
    "Minimum ROE",
    float(df["roe"].min()),
    float(df["roe"].max()),
    float(df["roe"].min())
)

max_pe = st.sidebar.slider(
    "Maximum PE Ratio",
    float(df["pe_ratio"].min()),
    float(df["pe_ratio"].max()),
    float(df["pe_ratio"].max())
)

max_de = st.sidebar.slider(
    "Maximum Debt / Equity",
    float(df["de_ratio"].min()),
    float(df["de_ratio"].max()),
    float(df["de_ratio"].max())
)

# Apply Filters
filtered = df[
    (df["roe"] >= min_roe) &
    (df["pe_ratio"] <= max_pe) &
    (df["de_ratio"] <= max_de)
]

# Search Filter
if search:
    filtered = filtered[
        filtered["company_name"].str.contains(search, case=False)
    ]

st.subheader("Filtered Companies")

st.dataframe(
    filtered[
        [
            "company_name",
            "ticker",
            "sector",
            "roe",
            "roa",
            "pe_ratio",
            "de_ratio"
        ]
    ],
    use_container_width=True
)

# Download Button
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="stock_screener.csv",
    mime="text/csv"
)