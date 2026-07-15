import streamlit as st

st.title("📊 Stock Screener")
st.sidebar.header("Filters")

roe = st.sidebar.slider(
    "Minimum ROE (%)",
    0,
    50,
    15
)

de = st.sidebar.slider(
    "Maximum D/E",
    0.0,
    5.0,
    1.0
)

fcf = st.sidebar.slider(
    "Minimum FCF",
    -5000,
    50000,
    0
)

revenue = st.sidebar.slider(
    "Revenue CAGR",
    0,
    50,
    10
)

pat = st.sidebar.slider(
    "PAT CAGR",
    0,
    50,
    10
)

opm = st.sidebar.slider(
    "Operating Margin",
    0,
    50,
    15
)

pe = st.sidebar.slider(
    "Maximum PE",
    0,
    100,
    25
)

pb = st.sidebar.slider(
    "Maximum PB",
    0.0,
    10.0,
    3.0
)

dividend = st.sidebar.slider(
    "Dividend Yield",
    0.0,
    10.0,
    1.0
)

icr = st.sidebar.slider(
    "Interest Coverage",
    0,
    20,
    5
)
st.subheader("Preset Screeners")

c1, c2, c3 = st.columns(3)

if c1.button("Quality"):
    st.success("Quality Screener Selected")

if c2.button("Value"):
    st.success("Value Screener Selected")

if c3.button("Growth"):
    st.success("Growth Screener Selected")

c4, c5, c6 = st.columns(3)

if c4.button("Dividend"):
    st.success("Dividend Screener Selected")

if c5.button("Debt-Free"):
    st.success("Debt-Free Screener Selected")

if c6.button("Turnaround"):
    st.success("Turnaround Screener Selected")
    
import pandas as pd

companies = pd.DataFrame({

    "Company":[
        "TCS",
        "Infosys",
        "HDFC Bank",
        "ITC",
        "Reliance"
    ],

    "ROE":[
        25,
        23,
        18,
        21,
        16
    ],

    "D/E":[
        0.2,
        0.1,
        1.3,
        0.0,
        0.4
    ],

    "Composite Score":[
        94,
        92,
        88,
        85,
        84
    ]

})

st.subheader("Results")

st.write(f"{len(companies)} Companies Found")

st.dataframe(
    companies,
    use_container_width=True
)
csv = companies.to_csv(index=False)

st.download_button(

    "Download CSV",

    csv,

    file_name="screener_results.csv",

    mime="text/csv"

)

st.write("Filter companies using financial metrics.")