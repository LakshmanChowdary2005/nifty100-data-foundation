import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.db import (
    get_companies,
    get_financial_ratios,
    get_profit_loss,
    get_balance_sheet,
    get_cashflow,
)

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Nifty100 Analytics Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Nifty100 Analytics Dashboard")
st.markdown("### Financial Analytics Dashboard")

# -------------------------------
# Load Data
# -------------------------------
companies = get_companies()
ratios = get_financial_ratios()
profit = get_profit_loss()
balance = get_balance_sheet()
cashflow = get_cashflow()

# -------------------------------
# KPI Cards
# -------------------------------
total_companies = len(companies)
avg_roe = ratios["roe"].mean()
avg_roa = ratios["roa"].mean()
avg_pe = ratios["pe_ratio"].mean()
avg_de = ratios["de_ratio"].mean()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("🏢 Companies", total_companies)
c2.metric("📊 Avg ROE", f"{avg_roe:.2f}%")
c3.metric("📈 Avg ROA", f"{avg_roa:.2f}%")
c4.metric("💰 Avg PE", f"{avg_pe:.2f}")
c5.metric("🏦 Avg D/E", f"{avg_de:.2f}")

st.divider()

# -------------------------------
# Company Sector Distribution
# -------------------------------
st.subheader("🏭 Company Distribution by Sector")

sector = (
    companies.groupby("sector")
    .size()
    .reset_index(name="Companies")
)

fig = px.pie(
    sector,
    names="sector",
    values="Companies",
    hole=0.45,
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -------------------------------
# Financial Ratio Comparison
# -------------------------------
st.subheader("📊 Average Financial Ratios")

ratio_df = {
    "Metric": ["ROE", "ROA", "PE Ratio", "Debt/Equity"],
    "Average": [
        avg_roe,
        avg_roa,
        avg_pe,
        avg_de,
    ],
}

ratio_fig = px.bar(
    ratio_df,
    x="Metric",
    y="Average",
    text="Average",
)

ratio_fig.update_traces(textposition="outside")

st.plotly_chart(ratio_fig, use_container_width=True)

st.divider()

# -------------------------------
# Latest Profit Table
# -------------------------------
st.subheader("💹 Latest Profit & Loss")

latest_profit = (
    profit.sort_values("year")
    .groupby("company_id")
    .tail(1)
)

latest_profit = latest_profit.merge(
    companies,
    on="company_id",
)

st.dataframe(
    latest_profit[
        [
            "company_name",
            "year",
            "sales",
            "net_profit",
        ]
    ],
    use_container_width=True,
)

st.divider()

# -------------------------------
# Latest Balance Sheet
# -------------------------------
st.subheader("🏦 Latest Balance Sheet")

latest_balance = (
    balance.sort_values("year")
    .groupby("company_id")
    .tail(1)
)

latest_balance = latest_balance.merge(
    companies,
    on="company_id",
)

st.dataframe(
    latest_balance[
        [
            "company_name",
            "year",
            "assets",
            "liabilities",
            "equity",
        ]
    ],
    use_container_width=True,
)

st.divider()

# -------------------------------
# Cash Flow Chart
# -------------------------------
st.subheader("💵 Operating Cash Flow")

latest_cf = (
    cashflow.sort_values("year")
    .groupby("company_id")
    .tail(1)
)

latest_cf = latest_cf.merge(
    companies,
    on="company_id",
)

cash_fig = px.bar(
    latest_cf,
    x="company_name",
    y="operating_cf",
    title="Operating Cash Flow",
)

st.plotly_chart(cash_fig, use_container_width=True)

st.divider()

# -------------------------------
# Company Data
# -------------------------------
st.subheader("📋 Company Master Data")

st.dataframe(companies, use_container_width=True)

st.success("Dashboard Loaded Successfully ✅")