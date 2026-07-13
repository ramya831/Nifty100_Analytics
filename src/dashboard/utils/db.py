import sqlite3
import pandas as pd
import streamlit as st

DB_PATH = "data/nifty100.db"


@st.cache_data(ttl=600)
def get_companies():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM companies", conn)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_ratios(ticker=None, year=None):
    conn = sqlite3.connect(DB_PATH)

    query = "SELECT * FROM financial_ratios"

    conditions = []

    if ticker:
        conditions.append(f"company_id='{ticker}'")

    if year:
        conditions.append(f"year='{year}'")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    df = pd.read_sql(query, conn)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_pl(ticker):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"SELECT * FROM profit_loss WHERE company_id='{ticker}'", conn
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_bs(ticker):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"SELECT * FROM balance_sheet WHERE company_id='{ticker}'", conn
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_cf(ticker):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"SELECT * FROM cash_flow WHERE company_id='{ticker}'", conn
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_sectors():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM sectors", conn)
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_peers(group_name):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"SELECT * FROM peer_percentiles WHERE peer_group_name='{group_name}'",
        conn
    )
    conn.close()
    return df


@st.cache_data(ttl=600)
def get_valuation(ticker):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(
        f"SELECT * FROM valuation WHERE company_id='{ticker}'",
        conn
    )
    conn.close()
    return df