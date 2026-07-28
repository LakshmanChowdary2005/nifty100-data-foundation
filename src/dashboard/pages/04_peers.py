import streamlit as st
import plotly.express as px
from utils.db import get_companies, get_financial_ratios

st.set_page_config(
    page_title="Peer Comparison",
    layout="wide"
)

st.title("👥 Peer Comparison")

companies = get_companies()
ratios = get_financial_ratios()

df = companies.merge(
    ratios,
    on="company_id"
)

selected = st.multiselect(
    "Select Companies",
    df["company_name"].unique()
)

if selected:

    compare = df[
        df["company_name"].isin(selected)
    ]

    st.subheader("Comparison Table")

    st.dataframe(
        compare[
            [
                "company_name",
                "ticker",
                "sector",
                "roe",
                "roa",
                "pe_ratio",
                "de_ratio"
            ]
        ],
        use_container_width=True
    )

    st.subheader("ROE Comparison")

    fig = px.bar(
        compare,
        x="company_name",
        y="roe",
        color="company_name",
        text="roe"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("PE Ratio Comparison")

    fig2 = px.bar(
        compare,
        x="company_name",
        y="pe_ratio",
        color="company_name",
        text="pe_ratio"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.subheader("Debt / Equity")

    fig3 = px.bar(
        compare,
        x="company_name",
        y="de_ratio",
        color="company_name",
        text="de_ratio"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

else:

    st.info("Please select at least one company.")