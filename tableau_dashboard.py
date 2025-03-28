import streamlit as st

st.title("📊 Tableau Dashboard")

# Replace with your actual Tableau Public URL
tableau_url = "https://public.tableau.com/views/YourDashboardName/Sheet1"
st.components.v1.iframe(tableau_url, height=600, width=1000)