import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "db/nifty100.db"

@st.cache_data(ttl=600)
def execute_query(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_companies():
    return execute_query("SELECT * FROM companies")

def get_financial_ratios():
    return execute_query("SELECT * FROM financial_ratios")

def get_profit_loss():
    return execute_query("SELECT * FROM profitandloss")

def get_balance_sheet():
    return execute_query("SELECT * FROM balancesheet")

def get_cashflow():
    return execute_query("SELECT * FROM cashflow")

def get_analysis():
    return execute_query("SELECT * FROM analysis")

def get_documents():
    return execute_query("SELECT * FROM documents")

def get_pros_cons():
    return execute_query("SELECT * FROM prosandcons")

def get_sectors():
    return execute_query("SELECT * FROM sectors")

def get_stock_prices():
    return execute_query("SELECT * FROM stock_prices")

def get_peer_groups():
    return execute_query("SELECT * FROM peer_groups")