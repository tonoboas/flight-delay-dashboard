import streamlit as st

st.set_page_config(page_title="Flight Delay Dashboard", layout="centered")

st.markdown("<h1 style='text-align: center;'>✈️ Welcome to the U.S. Flight Delay Dashboard</h1>", unsafe_allow_html=True)
st.markdown("## ")
st.markdown("### Use the buttons below to get started:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔮 Predict Flight Delays"):
        st.switch_page("flight_prediction.py")

with col2:
    if st.button("📊 Explore Dashboard"):
        st.switch_page("tableau_dashboard.py")