import streamlit as st
import numpy as np
import joblib

# 🚨 Set page config FIRST
st.set_page_config(page_title="Flight Prediction", layout="centered")

# 🌤️ Sky blue background
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;
    }
    .stApp {
        background-color: #e0f7fa;
        background-attachment: fixed;
        background-size: cover;
    }
    h1, h3 {
        text-align: center;
        color: #003366;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
model = joblib.load("ridge_model.pkl")

# Categorical variables
airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']
dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

# Page header
st.markdown("<h1>✈️ FLIGHT DELAY FORECAST</h1>", unsafe_allow_html=True)
st.markdown("### 📝 Fill in the flight and weather details below:")

# Flight Info Inputs
st.markdown("Select the day of the week (1 = Monday, 7 = Sunday)")
day_of_week = st.slider("", 1, 7, 3)

st.markdown("Select the month of departure (1 = January, 12 = December)")
month = st.slider("", 1, 12, 6)

airline = st.selectbox("Choose your airline:", airline_cats)
dep_time = st.selectbox("Pick the time of departure:", dep_time_cats)
dep_air = st.selectbox("Departure airport code:", major_airports)
arr_air = st.selectbox("Arrival airport code:", major_airports)

# Weather Info Inputs
st.markdown("Enter weather conditions at departure:")
tavg = st.number_input("Average Temperature (°C) — usually -10°C to 40°C", value=15.0)
prcp = st.number_input("Precipitation (mm) — 0.0 means clear skies", value=0.0)
snow = st.number_input("Snowfall (mm) — 0 if none", value=0.0)
wdir = st.number_input("Wind Direction (0–360°)", value=180.0)
wspd = st.number_input("Wind Speed (km/h) — usually 0 to 50", value=12.0)

# Encode features
features = np.array([[
    day_of_week, month,
    airline_cats.index(airline),
    dep_time_cats.index(dep_time),
    major_airports.index(dep_air),
    major_airports.index(arr_air),
    tavg, prcp, snow, wdir, wspd
]])

# Predict button
if st.button("📍 Predict Delay"):
    pred_log = model.predict(features)[0]
    pred_delay = np.expm1(pred_log)
    st.success(f"🕒 Predicted Departure Delay: **{pred_delay:.2f} minutes**")