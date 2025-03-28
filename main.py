import streamlit as st

st.set_page_config(page_title="Flight Dashboard", layout="centered")

st.markdown("## ✈️ Welcome to the U.S. Flight Dashboard System")
st.write("Use the buttons below to navigate:")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href="/pages/flight_prediction" target="_self">
            <button style="font-size:20px;padding:10px 24px;">🔮 Predict Flight Delays</button>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <a href="/pages/tableau_dashboard" target="_self">
            <button style="font-size:20px;padding:10px 24px;">📊 Explore Dashboard</button>
        </a>
        """,
        unsafe_allow_html=True,
    )