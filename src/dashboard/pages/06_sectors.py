import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏢 Sector Analysis")

sector = st.selectbox(
    "Select Sector",
    ["IT", "Banking", "FMCG", "Energy"]
)

df = pd.DataFrame({
    "Company": ["TCS", "Infosys", "Wipro", "HCL"],
    "Revenue": [200, 180, 150, 170],
    "ROE": [22, 20, 18, 19],
    "MarketCap": [1500, 1200, 800, 900]
})

fig = px.scatter(
    df,
    x="Revenue",
    y="ROE",
    size="MarketCap",
    hover_name="Company"
)

st.plotly_chart(fig, width="stretch")