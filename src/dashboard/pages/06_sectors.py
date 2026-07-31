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

with st.spinner("Loading Sector Analysis..."):
    companies = get_companies()
    ratios = get_financial_ratios()

# -----------------------------
# KPI Cards
# -----------------------------

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Total Companies",
    len(df)
)

k2.metric(
    "Total Sectors",
    df["sector"].nunique()
)

k3.metric(
    "Average ROE",
    f"{df['roe'].mean():.2f}%"
)

k4.metric(
    "Average PE",
    f"{df['pe_ratio'].mean():.2f}"
)

st.divider()

# Merge company and ratio data
df = companies.merge(ratios, on="company_id")

# -----------------------------
# Sector Distribution
# -----------------------------
st.subheader("📊 Companies by Sector")
st.subheader("📌 Sector Performance Bubble Chart")

fig_bubble = px.scatter(
    df,
    x="pe_ratio",
    y="roe",
    size="roa",
    color="sector",
    hover_name="company_name",
    title="ROE vs PE Ratio"
)

st.plotly_chart(
    fig_bubble,
    use_container_width=True
)

st.divider()

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
st.subheader("📈 Sector Summary")

summary = sector_df[
    [
        "roe",
        "roa",
        "pe_ratio",
        "de_ratio"
    ]
].mean()

st.table(summary)
best = sector_df.sort_values(
    "roe",
    ascending=False
).iloc[0]

st.success(
    f"""
🏆 Best Company

{best['company_name']}

ROE : {best['roe']:.2f}%
"""
)
st.divider()

st.caption(
    "📈 Nifty100 Analytics Dashboard | Sector Analysis | Sprint 4"
)