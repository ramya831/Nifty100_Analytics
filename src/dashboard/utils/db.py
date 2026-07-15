import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "db/nifty100.db"


# Cache the database connection
@st.cache_resource
def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)


# -------------------------------
# Companies
# -------------------------------
@st.cache_data(ttl=600)
def get_companies():
    df = pd.read_excel(
        "data/raw/companies.xlsx",
        header=1
    )
    return df


# -------------------------------
# Financial Ratios
# -------------------------------
@st.cache_data(ttl=600)
def get_ratios():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM financial_ratios", conn)


# -------------------------------
# Profit & Loss
# -------------------------------
@st.cache_data(ttl=600)
def get_profit_loss():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM profitandloss", conn)


# -------------------------------
# Balance Sheet
# -------------------------------
@st.cache_data(ttl=600)
def get_balance_sheet():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM balancesheet", conn)


# -------------------------------
# Cash Flow
# -------------------------------
@st.cache_data(ttl=600)
def get_cash_flow():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM cashflow", conn)


# -------------------------------
# Sectors
# -------------------------------
@st.cache_data(ttl=600)
def get_sectors():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM sectors", conn)


# -------------------------------
# Peer Groups
# -------------------------------
@st.cache_data(ttl=600)
def get_peer_groups():
    conn = get_connection()
    return pd.read_sql_query("SELECT * FROM peer_groups", conn)