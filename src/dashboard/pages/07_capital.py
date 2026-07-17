import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Capital Allocation")

df = pd.DataFrame({
    "Pattern": [
        "Reinvestor",
        "Debt Funded",
        "Cash Accumulator",
        "Mixed"
    ],
    "Companies": [25, 18, 30, 19]
})

fig = px.treemap(
    df,
    path=["Pattern"],
    values="Companies"
)

st.plotly_chart(fig, width="stretch")