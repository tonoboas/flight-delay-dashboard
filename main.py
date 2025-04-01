import streamlit as st
import numpy as np
import joblib

# Set the page config FIRST!
st.set_page_config(page_title="Flight Delay Predictor", layout="centered")

# Load the trained Ridge regression model
model = joblib.load("ridge_model.pkl")

# Categories
airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']

dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

# Title
st.markdown("<h1 style='text-align: center; font-size: 42px;'>✈️ FLIGHT DELAY FORECAST</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>📝 Fill in the flight and weather details below:</h3>", unsafe_allow_html=True)
st.markdown("---")

# Inputs
day_of_week = st.slider("Select the day of the week (1 = Monday, 7 = Sunday)", 1, 7, 3)
month = st.slider("Select the month of departure (1 = January, 12 = December)", 1, 12, 6)

airline = st.selectbox("Choose your airline", airline_cats)
dep_time = st.selectbox("Pick the time of departure", dep_time_cats)
dep_air = st.selectbox("Departure airport code", major_airports)
arr_air = st.selectbox("Arrival airport code", major_airports)

tavg = st.number_input("Avg Temperature (°C) — typically between -10 and 40", value=15.0)
prcp = st.number_input("Precipitation (mm) — often 0 to 20+", value=0.0)
snow = st.number_input("Snowfall (mm) — usually 0 to 10+", value=0.0)
wdir = st.number_input("Wind Direction (0 to 360 degrees)", value=180.0)
wspd = st.number_input("Wind Speed (km/h) — usually 0 to 50", value=12.0)

# Encoding
airline_code = airline_cats.index(airline)
dep_time_code = dep_time_cats.index(dep_time)
dep_air_code = major_airports.index(dep_air)
arr_air_code = major_airports.index(arr_air)

features = np.array([[day_of_week, month, airline_code, dep_time_code,
                      dep_air_code, arr_air_code, tavg, prcp, snow, wdir, wspd]])

# Prediction
if st.button("🔮 Predict Delay"):
    pred_log = model.predict(features)[0]
    pred_delay = np.expm1(pred_log)
    st.success(f"🕰️ Predicted Departure Delay: **{pred_delay:.2f} minutes**")