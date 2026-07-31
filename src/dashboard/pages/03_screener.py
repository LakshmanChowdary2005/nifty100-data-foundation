import streamlit as st
from utils.db import get_companies, get_financial_ratios

st.set_page_config(page_title="Stock Screener", layout="wide")

st.title("🔍 Stock Screener")

# Load Data
with st.spinner("Loading Screener..."):
    companies = get_companies()
    ratios = get_financial_ratios()

# Merge company details with ratios

df = companies.merge(
    ratios,
    on="company_id"
)

# -------------------------------
# Quality Score
# -------------------------------

df["quality_score"] = (
    df["roe"] * 0.40 +
    df["roa"] * 0.30 +
    (1 / df["de_ratio"].replace(0, 0.1)) * 10 +
    (1 / df["pe_ratio"].replace(0, 1)) * 20
)

st.sidebar.subheader("Quick Presets")

preset = st.sidebar.radio(
    "Select Preset",
    [
        "Custom",
        "Quality",
        "Growth",
        "Value",
        "Debt-Free"
    ]
)

# -----------------------------
# Preset Values
# -----------------------------

if preset == "Quality":

    roe_default = 20.0
    pe_default = 30.0
    de_default = 0.5

elif preset == "Growth":

    roe_default = 15.0
    pe_default = float(df["pe_ratio"].max())
    de_default = 1.0

elif preset == "Value":

    roe_default = 10.0
    pe_default = 20.0
    de_default = 1.0

elif preset == "Debt-Free":

    roe_default = 10.0
    pe_default = float(df["pe_ratio"].max())
    de_default = 0.1

else:

    roe_default = float(df["roe"].min())
    pe_default = float(df["pe_ratio"].max())
    de_default = float(df["de_ratio"].max())

# -----------------------------
# Search Box
# -----------------------------

search = st.sidebar.text_input("Search Company")


# Sliders
min_roe = st.sidebar.slider(
    "Minimum ROE",
    float(df["roe"].min()),
    float(df["roe"].max()),
    roe_default
)

max_pe = st.sidebar.slider(
    "Maximum PE Ratio",
    float(df["pe_ratio"].min()),
    float(df["pe_ratio"].max()),
    pe_default
)

max_de = st.sidebar.slider(
    "Maximum Debt / Equity",
    float(df["de_ratio"].min()),
    float(df["de_ratio"].max()),
    de_default
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

st.subheader("📋 Filtered Companies")

st.success(
    f"✅ {len(filtered)} companies match your filters."
)
st.info(
    f"""
### Current Filters

- Minimum ROE : {min_roe:.2f}
- Maximum PE : {max_pe:.2f}
- Maximum D/E : {max_de:.2f}
"""
)

st.dataframe(
    filtered[
        [
            "company_name",
            "ticker",
            "sector",
            "roe",
            "roa",
            "pe_ratio",
            "de_ratio",
            "quality_score"
        ]
    ].sort_values(
        "quality_score",
        ascending=False
    ),
    use_container_width=True
)

# Download Button
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="nifty100_stock_screener.csv",
    mime="text/csv"
)
st.divider()

st.caption(
    "📈 Nifty100 Analytics Dashboard | Stock Screener | Sprint 4"
)