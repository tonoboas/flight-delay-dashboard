import streamlit as st

st.set_page_config(page_title="Flight Dashboard", layout="centered")

st.markdown("## 🛫 Welcome to the U.S. Flight Dashboard System")
st.write("Use the menu on the left to:")

st.markdown("- 🔮 **[Predict flight delays](pages/flight_prediction.py)**")
st.markdown("- 📊 **[Explore our interactive dashboard](pages/tableau_dashboard.py)**")
