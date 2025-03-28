import streamlit as st
import numpy as np
import joblib

model = joblib.load("ridge_model.pkl")

airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']

dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

st.title("🔮 Flight Delay Predictor")

day_of_week = st.slider("Day of Week (1=Mon ... 7=Sun)", 1, 7, 3)
month = st.slider("Month", 1, 12, 6)
airline = st.selectbox("Airline", airline_cats)
dep_time = st.selectbox("Departure Time", dep_time_cats)
dep_air = st.selectbox("Departure Airport", major_airports)
arr_air = st.selectbox("Arrival Airport", major_airports)

tavg = st.number_input("Avg Temp (°C)", value=15.0)
prcp = st.number_input("Precipitation (mm)", value=0.0)
snow = st.number_input("Snowfall (mm)", value=0.0)
wdir = st.number_input("Wind Direction", value=180.0)
wspd = st.number_input("Wind Speed", value=12.0)

airline_code = airline_cats.index(airline)
dep_time_code = dep_time_cats.index(dep_time)
dep_air_code = major_airports.index(dep_air)
arr_air_code = major_airports.index(arr_air)

features = np.array([[day_of_week, month, airline_code, dep_time_code,
                      dep_air_code, arr_air_code, tavg, prcp, snow, wdir, wspd]])

if st.button("Predict Delay"):
    pred_log = model.predict(features)[0]
    pred_delay = np.expm1(pred_log)
    st.success(f"Predicted Departure Delay: {pred_delay:.2f} minutes")