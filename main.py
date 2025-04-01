from pathlib import Path

improved_code = """
import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Flight Delay Forecast", layout="centered")

# Load model
model = joblib.load("ridge_model.pkl")

# Custom CSS for styling
st.markdown(\"""
    <style>
        .main {
            background-color: #e6f2ff;
            padding: 2rem;
        }
        h1 {
            text-align: center;
            font-size: 3em;
            color: #003366;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stSlider > div {
            padding-bottom: 10px;
        }
        .stSelectbox > div {
            padding-bottom: 10px;
        }
    </style>
\""", unsafe_allow_html=True)

# Title
st.markdown("<h1>✈️ Flight Delay Forecast</h1>", unsafe_allow_html=True)

# Categories
airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']

dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

# User inputs
st.subheader("Flight Info")
day_of_week = st.slider("Day of Week (1 = Monday ... 7 = Sunday)", 1, 7, 3)
month = st.slider("Month of Flight (1 = Jan ... 12 = Dec)", 1, 12, 6)
airline = st.selectbox("Select the Airline Carrier", airline_cats)
dep_time = st.selectbox("Select Time of Departure", dep_time_cats)
dep_air = st.selectbox("Departure Airport", major_airports)
arr_air = st.selectbox("Arrival Airport", major_airports)

st.subheader("Weather Conditions")
st.markdown("🌡️ **Temperature Range:** -30°C to 50°C")
tavg = st.number_input("Average Temperature (°C)", value=15.0, min_value=-30.0, max_value=50.0)

st.markdown("🌧️ **Precipitation Range:** 0 to 100 mm")
prcp = st.number_input("Precipitation (mm)", value=0.0, min_value=0.0, max_value=100.0)

st.markdown("❄️ **Snowfall Range:** 0 to 100 mm")
snow = st.number_input("Snowfall (mm)", value=0.0, min_value=0.0, max_value=100.0)

st.markdown("🧭 **Wind Direction:** Degrees from North (0° to 360°)")
wdir = st.number_input("Wind Direction (°)", value=180.0, min_value=0.0, max_value=360.0)

st.markdown("🍃 **Wind Speed Range:** 0 to 150 km/h")
wspd = st.number_input("Wind Speed (km/h)", value=12.0, min_value=0.0, max_value=150.0)

# Encode categorical features
airline_code = airline_cats.index(airline)
dep_time_code = dep_time_cats.index(dep_time)
dep_air_code = major_airports.index(dep_air)
arr_air_code = major_airports.index(arr_air)

# Feature array
features = np.array([[day_of_week, month, airline_code, dep_time_code,
                      dep_air_code, arr_air_code, tavg, prcp, snow, wdir, wspd]])

# Prediction
if st.button("🚀 Predict Delay"):
    pred_log = model.predict(features)[0]
    pred_delay = np.expm1(pred_log)
    st.success(f"⏰ Estimated Departure Delay: **{pred_delay:.2f} minutes**")
"""

# Save the improved code to a Python file
file_path = Path("/mnt/data/main.py")
file_path.write_text(improved_code)
file_path