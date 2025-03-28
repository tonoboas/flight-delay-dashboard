import streamlit as st

st.set_page_config(page_title="Flight Dashboard", layout="centered")

st.markdown("## ✈️ Welcome to the U.S. Flight Dashboard System")
st.write("Use the buttons below to navigate:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔮 Predict Flight Delays"):
        st.switch_page("pages/flight_prediction.py")

with col2:
    if st.button("📊 Explore Dashboard"):
        st.switch_page("pages/tableau_dashboard.py")