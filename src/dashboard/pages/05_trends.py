import streamlit as st
import plotly.express as px
from utils.db import (
    get_companies,
    get_profit_loss,
    get_balance_sheet,
    get_cashflow,
)

st.set_page_config(page_title="Trend Analysis", layout="wide")

st.title("📈 Trend Analysis")

with st.spinner("Loading Trend Analysis..."):
    companies = get_companies()
    profit = get_profit_loss()
    balance = get_balance_sheet()
    cashflow = get_cashflow()

st.sidebar.header("Company Search")

search = st.sidebar.text_input(
    "🔍 Search Company"
)

company_list = companies["company_name"].sort_values()

if search:

    company_list = company_list[
        company_list.str.contains(
            search,
            case=False
        )
    ]

company = st.sidebar.selectbox(
    "Select Company",
    company_list
)

company_id = companies.loc[
    companies["company_name"] == company,
    "company_id"
].values[0]

# Filter Data
# Filter Data
profit_df = profit[profit["company_id"] == company_id]

# Sort by Year
profit_df = profit_df.sort_values("year")

# Calculate Year-over-Year Growth
profit_df["Sales Growth %"] = (
    profit_df["sales"].pct_change() * 100
)

profit_df["Profit Growth %"] = (
    profit_df["net_profit"].pct_change() * 100
)

balance_df = balance[balance["company_id"] == company_id]
cash_df = cashflow[cashflow["company_id"] == company_id]

# -------------------------------
# KPI Cards
# -------------------------------

latest_profit = profit_df.sort_values("year").iloc[-1]
latest_balance = balance_df.sort_values("year").iloc[-1]
latest_cash = cash_df.sort_values("year").iloc[-1]

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Sales",
    f"{latest_profit['sales']:.2f}"
)

k2.metric(
    "Net Profit",
    f"{latest_profit['net_profit']:.2f}"
)

k3.metric(
    "Assets",
    f"{latest_balance['assets']:.2f}"
)

k4.metric(
    "Operating CF",
    f"{latest_cash['operating_cf']:.2f}"
)

st.divider()

# ---------------- Sales Trend ----------------

st.subheader("📊 Multi Metric Trend")

metrics = st.multiselect(
    "Select up to 3 Metrics",
    [
        "sales",
        "net_profit"
    ],
    default=["sales"]
)


# ---------------- Net Profit ----------------

st.subheader("💰 Net Profit Trend")

fig2 = px.line(
    profit_df,
    x="year",
    y="net_profit",
    markers=True,
    title="Net Profit"
)

st.plotly_chart(fig2, use_container_width=True)
st.subheader("📈 Year-over-Year Growth")

st.dataframe(
    profit_df[
        [
            "year",
            "Sales Growth %",
            "Profit Growth %"
        ]
    ],
    use_container_width=True
)

fig1 = px.line(
    profit_df,
    x="year",
    y=metrics,
    markers=True,
    title="Selected Financial Metrics"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)
st.subheader("💰 Net Profit Trend")
fig2 = px.line(
    profit_df,
    x="year",
    y="net_profit",
    markers=True,
    title="Net Profit"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Balance Sheet ----------------

st.subheader("🏦 Assets vs Liabilities vs Equity")

fig3 = px.line(
    balance_df,
    x="year",
    y=["assets", "liabilities", "equity"],
    markers=True,
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- Cash Flow ----------------

st.subheader("💵 Cash Flow Trend")

fig4 = px.line(
    cash_df,
    x="year",
    y=[
        "operating_cf",
        "investing_cf",
        "financing_cf",
    ],
    markers=True,
)

st.plotly_chart(fig4, use_container_width=True)