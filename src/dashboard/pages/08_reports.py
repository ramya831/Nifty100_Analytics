import streamlit as st
import pandas as pd

st.title("📄 Annual Reports")

company = st.selectbox(
    "Select Company",
    ["TCS", "Infosys", "Reliance"]
)

df = pd.DataFrame({
    "Year": [2022, 2023, 2024],
    "Status": ["Available", "Available", "Available"],
    "Report Link": [
        "Annual_Report_2022.pdf",
        "Annual_Report_2023.pdf",
        "Annual_Report_2024.pdf"
    ]
})

st.dataframe(df, width="stretch")