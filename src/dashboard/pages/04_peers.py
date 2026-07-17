import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("👥 Peer Comparison")

# -----------------------------
# Peer Group Selection
# -----------------------------
group = st.selectbox(
    "Select Peer Group",
    ["IT", "Banking", "Auto", "Energy", "FMCG"]
)

# -----------------------------
# Sample Data
# -----------------------------
peer_data = {

    "IT": {
        "Company": ["TCS", "Infosys", "Wipro", "HCL Tech"],
        "ROE": [25, 22, 18, 20],
        "ROCE": [30, 28, 24, 26],
        "NPM": [20, 18, 16, 17],
        "DE": [0.20, 0.10, 0.30, 0.25],
        "FCF": [12000, 9500, 7200, 8100],
        "PAT CAGR": [18, 16, 12, 14],
        "Revenue CAGR": [15, 14, 10, 12],
        "Score": [94, 92, 84, 86]
    },

    "Banking": {
        "Company": ["HDFC Bank", "ICICI Bank", "SBI", "Axis Bank"],
        "ROE": [18, 17, 15, 16],
        "ROCE": [20, 19, 17, 18],
        "NPM": [24, 22, 18, 20],
        "DE": [5.5, 5.1, 6.2, 5.8],
        "FCF": [8000, 7200, 6500, 6100],
        "PAT CAGR": [12, 13, 10, 11],
        "Revenue CAGR": [10, 11, 8, 9],
        "Score": [91, 90, 86, 87]
    },

    "Auto": {
        "Company": ["Maruti", "Tata Motors", "M&M", "Bajaj Auto"],
        "ROE": [21, 19, 20, 24],
        "ROCE": [24, 22, 23, 28],
        "NPM": [11, 9, 12, 15],
        "DE": [0.10, 0.50, 0.30, 0.20],
        "FCF": [6200, 7100, 6800, 7500],
        "PAT CAGR": [14, 13, 15, 18],
        "Revenue CAGR": [12, 13, 14, 16],
        "Score": [90, 88, 89, 93]
    },

    "Energy": {
        "Company": ["Reliance", "ONGC", "BPCL", "IOC"],
        "ROE": [15, 12, 11, 10],
        "ROCE": [17, 14, 13, 12],
        "NPM": [13, 11, 9, 8],
        "DE": [0.40, 0.20, 0.50, 0.60],
        "FCF": [15000, 8400, 6200, 6100],
        "PAT CAGR": [10, 9, 8, 7],
        "Revenue CAGR": [9, 8, 7, 6],
        "Score": [92, 84, 82, 80]
    },

    "FMCG": {
        "Company": ["HUL", "Nestle", "ITC", "Britannia"],
        "ROE": [28, 35, 24, 30],
        "ROCE": [34, 40, 29, 36],
        "NPM": [18, 22, 28, 19],
        "DE": [0.05, 0.02, 0.00, 0.10],
        "FCF": [5400, 6100, 6800, 5900],
        "PAT CAGR": [14, 16, 13, 15],
        "Revenue CAGR": [11, 12, 10, 11],
        "Score": [93, 96, 91, 94]
    }

}

# -----------------------------
# Selected Group
# -----------------------------
data = peer_data[group]

st.subheader(f"Selected Peer Group: {group}")

# -----------------------------
# Radar Chart
# -----------------------------
company = data["Company"][0]

fig = go.Figure()

fig.add_trace(
    go.Scatterpolar(
        r=[
            data["ROE"][0],
            data["ROCE"][0],
            data["NPM"][0],
            data["DE"][0],
            data["PAT CAGR"][0],
            data["Revenue CAGR"][0],
            data["Score"][0]
        ],
        theta=[
            "ROE",
            "ROCE",
            "NPM",
            "D/E",
            "PAT CAGR",
            "Revenue CAGR",
            "Composite Score"
        ],
        fill="toself",
        name=company
    )
)

fig.update_layout(
    title=f"{company} Performance Radar",
    polar=dict(
        radialaxis=dict(
            visible=True
        )
    ),
    showlegend=True
)

st.plotly_chart(fig, width="stretch")

# -----------------------------
# Peer Comparison Table
# -----------------------------
df = pd.DataFrame({

    "Company": data["Company"],
    "Sector": [group] * 4,
    "ROE (%)": data["ROE"],
    "ROCE (%)": data["ROCE"],
    "Net Profit Margin (%)": data["NPM"],
    "Debt/Equity": data["DE"],
    "PAT CAGR (%)": data["PAT CAGR"],
    "Revenue CAGR (%)": data["Revenue CAGR"],
    "Composite Score": data["Score"]

})

st.subheader("Peer Comparison Table")

st.dataframe(df, width="stretch")

# -----------------------------
# Benchmark Company
# -----------------------------
best_company = df.loc[df["Composite Score"].idxmax(), "Company"]

st.success(f"🏆 Benchmark Company : {best_company}")

# -----------------------------
# Summary
# -----------------------------
st.info(f"Showing comparison for {len(df)} companies in the {group} sector.")