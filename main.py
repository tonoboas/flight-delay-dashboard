import streamlit as st
import numpy as np
import joblib

# Set page config
st.set_page_config(page_title="Flight Prediction", layout="centered")

# Inject custom CSS for sky blue background
st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa;
    }
    .stApp {
        background-color: #e0f7fa;
    }
    h1, h2, h3 {
        color: #003366;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
model = joblib.load("ridge_model.pkl")

# Categorical inputs
airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']

dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

# Header
st.markdown("<h1 style='text-align: center;'>✈️ FLIGHT DELAY FORECAST</h1>", unsafe_allow_html=True)
st.markdown("### 📝 Fill in the flight and weather details below:")

# Inputs
st.markdown("Select the day of the week (1 = Monday, 7 = Sunday)")
day_of_week = st.slider("Day of Week", 1, 7, 3)

st.markdown("Select the month of departure")
month = st.slider("Month", 1, 12, 6)

airline = st.selectbox("Choose your airline", airline_cats)
dep_time = st.selectbox("Pick the time of departure", dep_time_cats)
dep_air = st.selectbox("Departure airport code", major_airports)
arr_air = st.selectbox("Arrival airport code", major_airports)

st.markdown("Enter weather conditions at departure:")
tavg = st.number_input("Average Temperature (°C) — Usually between -10°C to 40°C", value=15.0)
prcp = st.number_input("Precipitation (mm) — 0.0 means clear skies", value=0.0)
snow = st.number_input("Snowfall (mm) — Enter 0 if not snowing", value=0.0)
wdir = st.number_input("Wind Direction (0–360°)", value=180.0)
wspd = st.number_input("Wind Speed (km/h) — Usually 0 to 50", value=12.0)

# Prepare model input
airline_code = airline_cats.index(airline)
dep_time_code = dep_time_cats.index(dep_time)
dep_air_code = major_airports.index(dep_air)
arr_air_code = major_airports.index(arr_air)

features = np.array([[day_of_week, month, airline_code, dep_time_code,
                      dep_air_code, arr_air_code, tavg, prcp, snow, wdir, wspd]])

# Prediction button
if st.button("📍 Predict Delay"):
    pred_log = model.predict(features)[0]
    pred_delay = np.expm1(pred_log)
    st.success(f"🕒 Predicted Departure Delay: **{pred_delay:.2f} minutes**")