import streamlit as st
from utils.db import (
    get_companies,
    get_financial_ratios,
    get_profit_loss,
    get_balance_sheet,
    get_cashflow,
    get_analysis,
)

st.set_page_config(page_title="Company Profile", layout="wide")

st.title("🏢 Company Profile")

companies = get_companies()
ratios = get_financial_ratios()
profit = get_profit_loss()
balance = get_balance_sheet()
cash = get_cashflow()
analysis = get_analysis()

company = st.selectbox(
    "Select Company",
    companies["company_name"].sort_values()
)

selected = companies[
    companies["company_name"] == company
].iloc[0]

company_id = selected["company_id"]

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Ticker", selected["ticker"])

with c2:
    st.metric("Sector", selected["sector"])

with c3:
    st.metric("Company ID", company_id)

st.divider()

ratio = ratios[ratios.company_id == company_id]

if not ratio.empty:

    a, b, c, d = st.columns(4)

    a.metric("ROE", f"{ratio['roe'].mean():.2f}%")

    b.metric("ROA", f"{ratio['roa'].mean():.2f}%")

    c.metric("PE Ratio", f"{ratio['pe_ratio'].mean():.2f}")

    d.metric("Debt / Equity", f"{ratio['de_ratio'].mean():.2f}")

st.divider()

st.subheader("📈 Profit & Loss")

st.dataframe(
    profit[profit.company_id == company_id],
    use_container_width=True,
)

st.subheader("🏦 Balance Sheet")

st.dataframe(
    balance[balance.company_id == company_id],
    use_container_width=True,
)

st.subheader("💰 Cash Flow")

st.dataframe(
    cash[cash.company_id == company_id],
    use_container_width=True,
)

st.subheader("⭐ Analysis")

st.dataframe(
    analysis[analysis.company_id == company_id],
    use_container_width=True,
)