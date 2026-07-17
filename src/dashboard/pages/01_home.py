import streamlit as st
import pandas as pd
import sqlite3

st.title("🏠 Home Dashboard")

year = st.sidebar.selectbox(
    "Select Year",
    [2019,2020,2021,2022,2023,2024],
    index=5
)

st.write("Selected Year:", year)

connection = sqlite3.connect("db/nifty100.db")

try:
    df = pd.read_sql(
        "SELECT * FROM financial_ratios",
        connection
    )

    st.success("Financial ratios loaded.")

except:
    df = pd.DataFrame()
    st.warning("financial_ratios table not found.")

connection.close()
col1, col2, col3 = st.columns(3)

col1.metric("Average ROE", "18.6%")
col2.metric("Median P/E", "24.1")
col3.metric("Median D/E", "0.62")

col4, col5, col6 = st.columns(3)

col4.metric("Companies", "92")
col5.metric("Revenue CAGR", "12.4%")
col6.metric("Debt Free", "37")
import plotly.express as px

sector = pd.DataFrame({
    "Sector": [
        "IT",
        "Banking",
        "Auto",
        "Energy",
        "FMCG",
        "Pharma"
    ],
    "Companies": [
        10,
        15,
        12,
        8,
        14,
        9
    ]
})

fig = px.pie(
    sector,
    values="Companies",
    names="Sector",
    hole=0.5
)

st.plotly_chart(fig, width="stretch")
st.subheader("Top 5 Companies")

top = pd.DataFrame({
    "Company": [
        "TCS",
        "Infosys",
        "Asian Paints",
        "Nestle",
        "HDFC Bank"
    ],
    "Composite Score": [
        94,
        92,
        91,
        90,
        89
    ]
})

st.dataframe(top, width="stretch")