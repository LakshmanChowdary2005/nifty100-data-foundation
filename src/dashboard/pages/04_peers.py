import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from utils.db import get_companies, get_financial_ratios

# Configure the Streamlit page
st.set_page_config(
    page_title="Peer Comparison", 
    layout="wide"
)

st.title("👥 Peer Comparison")

with st.spinner("Loading Peer Comparison..."):
    # Fetch data from source functions
    df_companies = get_companies()
    df_ratios = get_financial_ratios()
    
    # Merge datasets on a common identifier (assumed 'company_id' or 'ticker')
    # Update the 'on' parameter if your database uses a different key
    join_key = "company_id" if "company_id" in df_companies.columns else "ticker"
    df = pd.merge(df_companies, df_ratios, on=join_key)

# -------------------------------
# Sector Filter
# -------------------------------
sector = st.sidebar.selectbox(
    "Select Sector", 
    ["All"] + sorted(df["sector"].unique().tolist())
)

if sector != "All":
    df = df[df["sector"] == sector]

selected = st.multiselect(
    "Select Companies", 
    options=df["company_name"].unique()
)

# Only render visualization if companies are selected
if selected:
    compare = df[df["company_name"].isin(selected)]
    
    if not compare.empty:
        # -------------------------------
        # Key Metrics KPI Blocks
        # -------------------------------
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Average ROE", f"{compare['roe'].mean():.2f}%")
        k2.metric("Average ROA", f"{compare['roa'].mean():.2f}%")
        k3.metric("Average PE", f"{compare['pe_ratio'].mean():.2f}")
        k4.metric("Average D/E", f"{compare['de_ratio'].mean():.2f}")
        
        st.divider()
        
        # -------------------------------
        # Best Performing Company
        # -------------------------------
        best = compare.sort_values("roe", ascending=False).iloc[0]
        st.success(
            f"🏆 Best Performer : {best['company_name']} (ROE : {best['roe']:.2f}%)"
        )
        
        st.divider()
        
        # -------------------------------
        # Comparison Table
        # -------------------------------
        st.subheader("Comparison Table")
        st.dataframe(
            compare[[
                "company_name", 
                "ticker", 
                "sector", 
                "roe", 
                "roa", 
                "pe_ratio", 
                "de_ratio"
            ]], 
            use_container_width=True
        )
        
        # -------------------------------
        # ROE Comparison Chart
        # -------------------------------
        st.subheader("ROE Comparison")
        fig_roe = px.bar(
            compare,
            x="company_name",
            y="roe",
            color="company_name",
            text=compare["roe"].map(lambda x: f"{x:.2f}%"),
            labels={"company_name": "Company", "roe": "ROE (%)"}
        )
        st.plotly_chart(fig_roe, use_container_width=True)
        
        # -------------------------------
        # Radar Chart
        # -------------------------------
        st.subheader("📊 Financial Radar Comparison")
        fig_radar = go.Figure()
        
        for _, row in compare.iterrows():
            fig_radar.add_trace(
                go.Scatterpolar(
                    r=[row["roe"], row["roa"], row["pe_ratio"], row["de_ratio"]],
                    theta=["ROE", "ROA", "PE Ratio", "Debt / Equity"],
                    fill="toself",
                    name=row["company_name"]
                )
            )
            
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True)
            ),
            showlegend=True,
            height=600
        )
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # -------------------------------
        # PE Ratio Comparison Chart
        # -------------------------------
        st.subheader("PE Ratio Comparison")
        fig2 = px.bar(
            compare, 
            x="company_name", 
            y="pe_ratio", 
            color="company_name", 
            text=compare["pe_ratio"].map(lambda x: f"{x:.2f}"),
            labels={"company_name": "Company", "pe_ratio": "P/E Ratio"}
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # -------------------------------
        # Debt / Equity Chart
        # -------------------------------
        st.subheader("Debt / Equity")
        fig3 = px.bar(
            compare, 
            x="company_name", 
            y="de_ratio", 
            color="company_name", 
            text=compare["de_ratio"].map(lambda x: f"{x:.2f}"),
            labels={"company_name": "Company", "de_ratio": "D/E Ratio"}
        )
        st.plotly_chart(fig3, use_container_width=True)

else:
    st.info("💡 Please select one or more companies from the dropdown to start the comparison.")

st.divider()
st.caption("📈 Nifty100 Analytics Dashboard | Peer Comparison | Sprint 4")
