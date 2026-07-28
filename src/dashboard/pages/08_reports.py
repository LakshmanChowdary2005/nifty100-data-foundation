import streamlit as st
from utils.db import get_companies, get_documents

st.set_page_config(
    page_title="Annual Reports",
    layout="wide"
)

st.title("📄 Annual Reports")

# Load data
companies = get_companies()
documents = get_documents()

# Merge company names with documents
df = documents.merge(
    companies,
    on="company_id"
)

# Company selection
company = st.selectbox(
    "Select Company",
    sorted(df["company_name"].unique())
)

filtered = df[df["company_name"] == company]

st.divider()

st.subheader("Company Information")

info = filtered.iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Company", info["company_name"])
col2.metric("Ticker", info["ticker"])
col3.metric("Sector", info["sector"])

st.divider()

st.subheader("Available Documents")

st.dataframe(
    filtered[
        [
            "document_type",
            "url"
        ]
    ],
    use_container_width=True
)

st.subheader("Open Report")

for _, row in filtered.iterrows():
    st.markdown(
        f"📄 **{row['document_type']}** - [Open Report]({row['url']})"
    )

st.success("Reports Loaded Successfully ✅")