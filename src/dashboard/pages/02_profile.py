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

with st.spinner("Loading Company Profile..."):
    companies = get_companies()
    ratios = get_financial_ratios()
    profit = get_profit_loss()
    balance = get_balance_sheet()
    cash = get_cashflow()
    analysis = get_analysis()

st.sidebar.header("Search Company")

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
    "Company",
    company_list
)

selected = companies[
    companies["company_name"] == company
].iloc[0]

company_id = selected["company_id"]

st.subheader("Company Information")

c1, c2, c3 = st.columns(3)

c1.metric(
    "🏢 Company",
    selected["company_name"]
)

c2.metric(
    "📈 Ticker",
    selected["ticker"]
)

c3.metric(
    "🏭 Sector",
    selected["sector"]
)

st.info(
    f"""
Company ID : {company_id}

This dashboard provides financial analysis,
cash flow,
balance sheet,
and performance indicators.
"""
)

st.divider()

with c1:
    st.metric("Ticker", selected["ticker"])

with c2:
    st.metric("Sector", selected["sector"])

with c3:
    st.metric("Company ID", company_id)

st.divider()

ratio = ratios[ratios.company_id == company_id]

if not ratio.empty:

    a, b, c, d, e = st.columns(5)

    a.metric(
    "ROE",
    f"{ratio['roe'].mean():.2f}%"
)

b.metric(
    "ROA",
    f"{ratio['roa'].mean():.2f}%"
)

c.metric(
    "PE Ratio",
    f"{ratio['pe_ratio'].mean():.2f}"
)

d.metric(
    "Debt/Equity",
    f"{ratio['de_ratio'].mean():.2f}"
)

quality = (
    ratio["roe"].mean()*0.6 +
    ratio["roa"].mean()*0.4
)

e.metric(
    "Quality Score",
    f"{quality:.2f}"
)

st.divider()

company_profit = profit[
    profit.company_id == company_id
]

st.dataframe(
    company_profit,
    use_container_width=True
)

import plotly.express as px

fig = px.line(
    company_profit,
    x="year",
    y=["sales","net_profit"],
    markers=True,
    title="Revenue vs Net Profit"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(
    profit[profit.company_id == company_id],
    use_container_width=True,
)

company_balance = balance[
    balance.company_id == company_id
]

st.dataframe(
    company_balance,
    use_container_width=True
)

fig = px.bar(
    company_balance,
    x="year",
    y=["assets","liabilities","equity"],
    barmode="group",
    title="Balance Sheet"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

company_cash = cash[
    cash.company_id == company_id
]

st.dataframe(
    company_cash,
    use_container_width=True
)

fig = px.bar(
    company_cash,
    x="year",
    y=[
        "operating_cf",
        "investing_cf",
        "financing_cf"
    ],
    barmode="group",
    title="Cash Flow"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

company_analysis = analysis[
    analysis.company_id == company_id
]

if not company_analysis.empty:

    latest = company_analysis.iloc[-1]

    st.success(
        f"""
Rating : {latest['rating']}

Remarks : {latest['remarks']}
"""
    )

st.dataframe(
    company_analysis,
    use_container_width=True
)
st.divider()

st.caption(
    "Nifty100 Analytics Dashboard | Company Profile"
)