import streamlit as st

st.set_page_config(
    page_title="Nifty100 Analytics",
    layout="wide"
)

pages = {
    "Home": "pages/01_home.py",
    "Company Profile": "pages/02_profile.py",
    "Screener": "pages/03_screener.py",
    "Peer Comparison": "pages/04_peers.py",
    "Trend Analysis": "pages/05_trends.py",
    "Sector Analysis": "pages/06_sectors.py",
    "Capital Allocation": "pages/07_capital.py",
    "Annual Reports": "pages/08_reports.py"
}

st.title("📈 Nifty100 Analytics")

page = st.sidebar.selectbox(
    "Navigation",
    list(pages.keys())
)

st.switch_page(pages[page])