import streamlit as st
import plotly.express as px
from utils.db import (
    get_companies,
    get_financial_ratios,
)

st.set_page_config(
    page_title="Sector Analysis",
    layout="wide"
)

st.title("🏭 Sector Analysis")

companies = get_companies()
ratios = get_financial_ratios()

# Merge company and ratio data
df = companies.merge(ratios, on="company_id")

# -----------------------------
# Sector Distribution
# -----------------------------
st.subheader("📊 Companies by Sector")

sector_count = (
    df.groupby("sector")
      .size()
      .reset_index(name="Companies")
)

fig = px.pie(
    sector_count,
    names="sector",
    values="Companies",
    hole=0.45,
    title="Sector Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Average ROE by Sector
# -----------------------------
st.subheader("📈 Average ROE by Sector")

avg_roe = (
    df.groupby("sector")["roe"]
      .mean()
      .reset_index()
)

fig2 = px.bar(
    avg_roe,
    x="sector",
    y="roe",
    color="sector",
    text="roe"
)

fig2.update_traces(texttemplate="%{text:.2f}")

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Average PE Ratio by Sector
# -----------------------------
st.subheader("💰 Average PE Ratio by Sector")

avg_pe = (
    df.groupby("sector")["pe_ratio"]
      .mean()
      .reset_index()
)

fig3 = px.bar(
    avg_pe,
    x="sector",
    y="pe_ratio",
    color="sector",
    text="pe_ratio"
)

fig3.update_traces(texttemplate="%{text:.2f}")

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Sector-wise Companies
# -----------------------------
st.subheader("🏢 Sector-wise Company List")

selected_sector = st.selectbox(
    "Select Sector",
    sorted(df["sector"].unique())
)

sector_df = df[df["sector"] == selected_sector]

st.dataframe(
    sector_df[
        [
            "company_name",
            "ticker",
            "roe",
            "roa",
            "pe_ratio",
            "de_ratio"
        ]
    ],
    use_container_width=True
)