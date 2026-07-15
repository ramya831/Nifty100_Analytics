import streamlit as st

st.title("👥 Peer Comparison")

group = st.selectbox(

    "Select Peer Group",

    [

        "IT",

        "Banking",

        "Auto",

        "Energy",

        "FMCG"

    ]

)
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatterpolar(

    r=[90,85,80,75,88,92,87,91],

    theta=[
        "ROE",
        "ROCE",
        "NPM",
        "D/E",
        "FCF",
        "PAT CAGR",
        "Revenue CAGR",
        "Score"
    ],

    fill="toself",

    name="TCS"

))

st.plotly_chart(

    fig,

    use_container_width=True

)

import pandas as pd

peer = pd.DataFrame({

    "Company":[

        "TCS",

        "Infosys",

        "Wipro",

        "HCL"

    ],

    "ROE":[

        25,

        22,

        18,

        20

    ],

    "Score":[

        94,

        92,

        84,

        86

    ]

})

st.subheader("Peer Comparison")

st.dataframe(

    peer,

    use_container_width=True

)

st.write("Selected Group:", group)