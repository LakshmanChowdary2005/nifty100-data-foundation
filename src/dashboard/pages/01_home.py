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
with st.spinner("Loading Dashboard..."):
    companies = get_companies()
    ratios = get_financial_ratios()
    profit = get_profit_loss()
    balance = get_balance_sheet()
    cashflow = get_cashflow()

# -------------------------------
# Year Selector
# -------------------------------

years = sorted(profit["year"].unique())

selected_year = st.sidebar.selectbox(
    "📅 Select Financial Year",
    years,
    index=len(years)-1
)

# -------------------------------
# KPI Cards
# -------------------------------
total_companies = len(companies)

avg_roe = ratios["roe"].mean()
avg_roa = ratios["roa"].mean()

avg_pe = ratios["pe_ratio"].mean()
median_pe = ratios["pe_ratio"].median()

avg_de = ratios["de_ratio"].mean()
median_de = ratios["de_ratio"].median()

debt_free = len(ratios[ratios["de_ratio"] <= 0.1])

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("🏢 Companies", total_companies)

c2.metric(
    "📊 Avg ROE",
    f"{avg_roe:.2f}%"
)

c3.metric(
    "📈 Avg ROA",
    f"{avg_roa:.2f}%"
)

c4.metric(
    "💰 Median PE",
    f"{median_pe:.2f}"
)

c5.metric(
    "🏦 Median D/E",
    f"{median_de:.2f}"
)

c6.metric(
    "✅ Debt Free",
    debt_free
)
# -------------------------------
# Quality Score Calculation
# -------------------------------

dashboard = companies.merge(ratios, on="company_id")

dashboard["quality_score"] = (
    dashboard["roe"] * 0.40 +
    dashboard["roa"] * 0.30 +
    (1 / dashboard["de_ratio"].replace(0, 0.1)) * 10 +
    (1 / dashboard["pe_ratio"].replace(0, 1)) * 20
)

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
    hole=0.55,
    title="Company Distribution by Sector"
)

fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Top 5 Companies
# -------------------------------

st.subheader("🏆 Top 5 Companies by Quality Score")

top5 = dashboard.sort_values(
    "quality_score",
    ascending=False
).head(5)

st.dataframe(
    top5[
        [
            "company_name",
            "sector",
            "roe",
            "roa",
            "pe_ratio",
            "de_ratio",
            "quality_score",
        ]
    ],
    use_container_width=True,
)

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

latest_profit = profit[profit["year"] == selected_year]

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

latest_balance = balance[
    balance["year"] == selected_year
]

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

latest_cf = cashflow[
    cashflow["year"] == selected_year
]

latest_cf = latest_cf.merge(
    companies,
    on="company_id",
)

latest_cf = latest_cf.sort_values(
    "operating_cf",
    ascending=False
)

cash_fig = px.bar(
    latest_cf.head(15),
    x="company_name",
    y="operating_cf",
    color="operating_cf",
    title="Top 15 Operating Cash Flow Companies",
)

cash_fig.update_layout(
    xaxis_title="Company",
    yaxis_title="Operating Cash Flow"
)

st.plotly_chart(cash_fig, use_container_width=True)

st.divider()

# -------------------------------
# Company Data
# -------------------------------
st.subheader("📋 Company Master Data")

st.dataframe(companies, use_container_width=True)

st.divider()

st.caption(
    "📈 Nifty100 Analytics Dashboard | Sprint 4 | Built with Streamlit, Plotly & SQLite"
)