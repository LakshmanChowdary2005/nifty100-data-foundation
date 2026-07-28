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

companies = get_companies()
profit = get_profit_loss()
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

# Filter Data
profit_df = profit[profit["company_id"] == company_id]
balance_df = balance[balance["company_id"] == company_id]
cash_df = cashflow[cashflow["company_id"] == company_id]

# ---------------- Sales Trend ----------------

st.subheader("📊 Sales Trend")

fig1 = px.line(
    profit_df,
    x="year",
    y="sales",
    markers=True,
    title="Sales"
)

st.plotly_chart(fig1, use_container_width=True)

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