import streamlit as st

st.title("🚗 Ford Car Price Prediction")

st.header("Enter Car Details")

# User Inputs
model = st.selectbox(
    "Select Model",
    ["Fiesta", "Focus", "Kuga", "EcoSport", "Mondeo", "Ka+", "B-Max", "C-Max"]
)

year = st.number_input(
    "Year",
    min_value=2000,
    max_value=2026,
    value=2020
)

mileage = st.number_input(
    "Mileage (Miles)",
    min_value=0,
    value=10000
)

engine_size = st.number_input(
    "Engine Size (Litres)",
    min_value=0.8,
    max_value=5.0,
    value=1.5,
    step=0.1
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic", "Semi-Auto"]
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "Electric"]
)

tax = st.number_input(
    "Tax",
    min_value=0,
    value=150
)

mpg = st.number_input(
    "MPG",
    min_value=0.0,
    value=50.0,
    step=0.1
)

if st.button("Predict Price"):
    st.success("Inputs received successfully!")

    st.write("### Entered Details")
    st.write("Model:", model)
    st.write("Year:", year)
    st.write("Mileage:", mileage)
    st.write("Engine Size:", engine_size)
    st.write("Transmission:", transmission)
    st.write("Fuel Type:", fuel_type)
    st.write("Tax:", tax)
    st.write("MPG:", mpg)