import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Flight Delay Forecast", layout="centered")

# Load the model
model = joblib.load("ridge_model.pkl")

# Categories
airline_cats = ['Alaska Airlines Inc.', 'Allegiant Air', 'American Airlines Inc.', 'American Eagle Airlines Inc.',
                'Delta Air Lines Inc', 'Endeavor Air', 'Frontier Airlines Inc.', 'Hawaiian Airlines Inc.',
                'JetBlue Airways', 'PSA Airlines', 'Republic Airways', 'Skywest Airlines Inc.',
                'Southwest Airlines Co.', 'Spirit Air Lines', 'United Air Lines Inc.']

dep_time_cats = ['Afternoon', 'Evening', 'Morning', 'Night']
major_airports = ["ATL", "LAX", "ORD", "DFW", "DEN"]

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background-color: #E6F0FA;
        }
        .big-font {
            font-size: 40px !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            font-weight: bold;
            color: #003366;
        }
        .instruction {
            font-size: 15px;
            color: #444;
            margin-bottom: 6px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-font">✈️ FLIGHT DELAY FORECAST</div>', unsafe_allow_html=True)
st.write("### ✏️ Fill in the flight and weather details below:")

# Inputs with instructions
st.markdown('<div class="instruction">Select the day of the week (1 = Monday, 7 = Sunday)</div>', unsafe_allow_html=True)
day_of_week = st.slider("Day of Week", 1, 7, 3)

st.markdown('<div class="instruction">Select the month of departure</div>', unsafe_allow_html=True)
month = st.slider("Month", 1, 12, 6)

st.markdown('<div class="instruction">Choose your airline</div>', unsafe_allow_html=True)
airline = st.selectbox("Airline", airline_cats)

st.markdown('<div class="instruction">Pick the time of departure</div>', unsafe_allow_html=True)
dep_time = st.selectbox("Departure Time", dep_time_cats)

st.markdown('<div class="instruction">Departure airport code</div>', unsafe_allow_html=True)
dep_air = st.selectbox("Departure Airport", major_airports)

st.markdown('<div class="instruction">Arrival airport code</div>', unsafe_allow_html=True)
arr_air = st.selectbox("Arrival Airport", major_airports)

st.markdown('<div class="instruction">Average temperature at departure time (°C). Range: -10 to 40</div>', unsafe_allow_html=True)
tavg = st.number_input("Avg Temp (°C)", min_value=-10.0, max_value=45.0, value=15.0)

st.markdown('<div class="instruction">Precipitation level in millimeters. Typical: 0–20 mm</div>', unsafe_allow_html=True)
prcp = st.number_input("Precipitation (mm)", min_value=0.0, max_value=100.0, value=0.0)

st.markdown('<div class="instruction">Snowfall in mm. Typical: 0–10 mm</div>', unsafe_allow_html=True)
snow = st.number_input("Snowfall (mm)", min_value=0.0, max_value=100.0, value=0.0)

st.markdown('<div class="instruction">Wind direction in degrees (0° = North, 90° = East)</div>', unsafe_allow_html=True)
wdir = st.number_input("Wind Direction", min_value=0.0, max_value=360.0, value=180.0)

st.markdown('<div class="instruction">Wind speed in km/h. Typical range: 0–50</div>', unsafe_allow_html=True)
wspd = st.number_input("Wind Speed", min_value=0.0, max_value=100.0, value=12.0)

# Feature transformation
airline_code = airline_cats.index(airline)
dep_time_code = dep_time_cats.index(dep_time)
dep_air_code = major_airports.index(dep_air)
arr_air_code = major_airports.index(arr_air)

features = np.array([[day_of_week, month, airline_code, dep_time_code,
                      dep_air_code, arr_air_code, tavg, prcp, snow, wdir, wspd]])

# Prediction
if st.button("🔮 Predict Delay"):
    with st.spinner("Calculating..."):
        pred_log = model.predict(features)[0]
        pred_delay = np.expm1(pred_log)
    st.success(f"✈️ Predicted Departure Delay: **{pred_delay:.2f} minutes**")