import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏢 Company Profile")

ticker = st.text_input("Enter Company Name or Ticker")

if ticker.upper() == "TCS":

    st.success(f"Showing details for {ticker}")

    st.markdown("### Company Information")

    st.write("**Company:**", ticker.upper())
    st.write("**Sector:** IT")
    st.write("**Sub Sector:** Software")
    st.write("**NSE:**", ticker.upper())
    st.write("Leading Indian IT Company")

    # KPI Cards
    c1, c2, c3 = st.columns(3)

    c1.metric("ROE", "24.6%")
    c2.metric("ROCE", "31.2%")
    c3.metric("NPM", "19.5%")

    c4, c5, c6 = st.columns(3)

    c4.metric("D/E", "0.18")
    c5.metric("Revenue CAGR", "15%")
    c6.metric("FCF", "₹12000 Cr")

    # Revenue Data
    revenue = pd.DataFrame({
        "Year": [2020, 2021, 2022, 2023, 2024],
        "Revenue": [150000, 165000, 180000, 200000, 220000]
    })

    revenue = revenue.fillna("N/A")

    if revenue.empty:
        st.warning("No Revenue Data Available")
    else:
        fig = px.bar(
            revenue,
            x="Year",
            y="Revenue",
            title="Revenue Growth"
        )
        st.plotly_chart(fig, width="stretch")

    # ROE Data
    roe = pd.DataFrame({
        "Year": [2020, 2021, 2022, 2023, 2024],
        "ROE": [18, 20, 21, 23, 25]
    })

    roe = roe.fillna("N/A")

    if roe.empty:
        st.warning("No ROE Data Available")
    else:
        fig = px.line(
            roe,
            x="Year",
            y="ROE",
            markers=True,
            title="ROE Trend"
        )
        st.plotly_chart(fig, width="stretch")

    # Pros
    st.subheader("Pros")

    st.success("✔ High ROE")
    st.success("✔ Strong Cash Flow")

    # Cons
    st.subheader("Cons")

    st.error("✖ Premium Valuation")
    st.error("✖ Slowing Revenue Growth")

elif ticker != "":
    st.error("Ticker not found - please try another.")

else:
    st.info("Please enter a company.")