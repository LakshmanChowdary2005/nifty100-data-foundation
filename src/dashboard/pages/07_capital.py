import streamlit as st
import plotly.express as px
from utils.db import (
    get_companies,
    get_balance_sheet,
    get_cashflow,
)

st.set_page_config(page_title="Capital Allocation", layout="wide")

st.title("💰 Capital Allocation Analysis")

with st.spinner("Loading Capital Allocation..."):
    companies = get_companies()
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

balance_df = balance[balance["company_id"] == company_id]
cash_df = cashflow[cashflow["company_id"] == company_id]

# ---------------- KPI Cards ----------------

latest_balance = balance_df.sort_values("year").tail(1)

if not latest_balance.empty:
    latest = latest_balance.iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🏦 Assets", f"{latest['assets']:,.0f}")
    c2.metric("📉 Liabilities", f"{latest['liabilities']:,.0f}")
    c3.metric("💼 Equity", f"{latest['equity']:,.0f}")
    capital = latest["assets"] - latest["liabilities"]

c4.metric(
    "Capital",
    f"{capital:,.0f}"
)

st.subheader("Capital Allocation Pattern")

if capital > latest["equity"]:

    st.success(
        "🟢 Strong Capital Allocation"
    )

elif capital > 0:

    st.warning(
        "🟡 Moderate Capital Allocation"
    )

else:

    st.error(
        "🔴 Weak Capital Allocation"
    )

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
st.subheader("Capital Summary")

summary = {
    "Assets": latest["assets"],
    "Liabilities": latest["liabilities"],
    "Equity": latest["equity"],
    "Capital": capital
}

st.table(summary)

# ---------------- Balance Sheet Table ----------------

st.subheader("Balance Sheet Data")

st.dataframe(
    balance_df,
    use_container_width=True
)
st.subheader("Capital Distribution")

tree = px.treemap(
    names=[
        "Assets",
        "Liabilities",
        "Equity"
    ],
    parents=[
        "",
        "",
        ""
    ],
    values=[
        latest["assets"],
        latest["liabilities"],
        latest["equity"]
    ]
)

st.plotly_chart(
    tree,
    use_container_width=True
)
st.divider()

st.caption(
    "📈 Nifty100 Analytics Dashboard | Capital Allocation | Sprint 4"
)