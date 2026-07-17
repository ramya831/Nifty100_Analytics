import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Trend Analysis")

company = st.selectbox(
    "Select Company",
    ["TCS", "Infosys", "Reliance", "ITC"]
)

metric = st.selectbox(
    "Select Metric",
    ["Revenue", "Net Profit", "ROE"]
)

df = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Revenue": [100, 120, 150, 180, 210],
    "Net Profit": [20, 25, 30, 35, 40],
    "ROE": [15, 16, 18, 19, 20]
})

fig = px.line(df, x="Year", y=metric, markers=True)

st.plotly_chart(fig, width="stretch")