import streamlit as st
import plotly.express as px
from utils.db import (
    get_companies,
    get_balance_sheet,
    get_cashflow,
)

st.set_page_config(page_title="Capital Allocation", layout="wide")

st.title("💰 Capital Allocation Analysis")

companies = get_companies()
balance = get_balance_sheet()
cashflow = get_cashflow()

company = st.selectbox(
    "Select Company",
    companies["company_name"].sort_values()
)

company_id = companies.loc[
    companies["company_name"] == company,
    "company_id"
].values[0]

balance_df = balance[balance["company_id"] == company_id]
cash_df = cashflow[cashflow["company_id"] == company_id]

# ---------------- KPI Cards ----------------

latest_balance = balance_df.sort_values("year").tail(1)

if not latest_balance.empty:
    latest = latest_balance.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric("🏦 Assets", f"{latest['assets']:,.0f}")
    c2.metric("📉 Liabilities", f"{latest['liabilities']:,.0f}")
    c3.metric("💼 Equity", f"{latest['equity']:,.0f}")

st.divider()

# ---------------- Assets/Liabilities/Equity ----------------

st.subheader("Assets vs Liabilities vs Equity")

fig1 = px.bar(
    balance_df,
    x="year",
    y=["assets", "liabilities", "equity"],
    barmode="group",
    title="Balance Sheet Comparison"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Cash Flow ----------------

st.subheader("Cash Flow Analysis")

fig2 = px.line(
    cash_df,
    x="year",
    y=[
        "operating_cf",
        "investing_cf",
        "financing_cf",
    ],
    markers=True,
    title="Cash Flow Trend"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Cash Flow Table ----------------

st.subheader("Cash Flow Data")

st.dataframe(
    cash_df,
    use_container_width=True
)

# ---------------- Balance Sheet Table ----------------

st.subheader("Balance Sheet Data")

st.dataframe(
    balance_df,
    use_container_width=True
)