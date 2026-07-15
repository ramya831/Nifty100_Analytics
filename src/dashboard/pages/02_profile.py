import streamlit as st

st.title("🏢 Company Profile")

ticker = st.text_input("Enter Company Name or Ticker")

if ticker.upper() == "TCS":

    st.success(f"Showing details for {ticker}")
    st.markdown("### Company Information")

    st.write("**Company:**", ticker)

    st.write("**Sector:** IT")

    st.write("**Sub Sector:** Software")

    st.write("**NSE:**", ticker.upper())

    st.write("Leading Indian IT Company")
    c1, c2, c3 = st.columns(3)

    c1.metric("ROE", "24.6%")
    c2.metric("ROCE", "31.2%")
    c3.metric("NPM", "19.5%")

    c4, c5, c6 = st.columns(3)

    c4.metric("D/E", "0.18")
    c5.metric("Revenue CAGR", "15%")
    c6.metric("FCF", "₹12000 Cr")
    import pandas as pd
    import plotly.express as px

    revenue = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Revenue": [150000, 165000, 180000, 200000, 220000]
    })

    fig = px.bar(
        revenue,
        x="Year",
        y="Revenue",
        title="Revenue Growth"
    )

    st.plotly_chart(fig, use_container_width=True)
    roe = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024],
    "ROE": [18, 20, 21, 23, 25]
    })

    fig = px.line(
        roe,
        x="Year",
        y="ROE",
        markers=True,
        title="ROE Trend"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Pros")

    st.success("✔ High ROE")

    st.success("✔ Strong Cash Flow")

    st.subheader("Cons")

    st.error("✖ Premium Valuation")

    st.error("✖ Slowing Revenue Growth")

elif ticker != "":
    st.error("Ticker not found - please try another.")

else:
    st.info("Please enter a company.")