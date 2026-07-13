import streamlit as st

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Nifty 100 Analytics",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# Dashboard Title
# ------------------------------
st.title("📊 Nifty 100 Analytics Dashboard")

st.markdown("""
Welcome to the **Nifty 100 Analytics Dashboard**.

Use the sidebar to navigate through the dashboard pages.
""")

st.success("Dashboard loaded successfully!")

st.sidebar.title("Navigation")
st.sidebar.success("Select a page from the Pages menu.")