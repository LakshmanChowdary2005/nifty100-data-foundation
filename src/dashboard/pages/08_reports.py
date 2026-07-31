import streamlit as st
from utils.db import get_companies, get_documents

st.set_page_config(
    page_title="Annual Reports",
    layout="wide"
)

st.title("📄 Annual Reports")

# Load data
with st.spinner("Loading Annual Reports..."):
    companies = get_companies()
    documents = get_documents()

# Merge company names with documents
df = documents.merge(
    companies,
    on="company_id"
)

# Company selection
st.sidebar.header("Company Search")

search = st.sidebar.text_input(
    "🔍 Search Company"
)

company_list = sorted(
    df["company_name"].unique()
)

if search:

    company_list = [
        c for c in company_list
        if search.lower() in c.lower()
    ]

company = st.sidebar.selectbox(
    "Select Company",
    company_list
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
st.metric(
    "📄 Total Reports",
    len(filtered)
)

st.divider()

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

    st.write(
        f"📄 {row['document_type']}"
    )

    st.link_button(
        "Open Report",
        row["url"]
    )

    st.divider()

st.success("Reports Loaded Successfully ✅")

st.divider()

st.caption(
    "📈 Nifty100 Analytics Dashboard | Annual Reports | Sprint 4"
)