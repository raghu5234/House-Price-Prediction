import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")
total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")
population = st.number_input("Population")
households = st.number_input("Households")
median_income = st.number_input("Median Income")

ocean = st.selectbox(
    "Ocean Proximity",
    ["INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN", "<1H OCEAN"]
)

# Convert the selected category into dummy variables
inland = 1 if ocean == "INLAND" else 0
island = 1 if ocean == "ISLAND" else 0
near_bay = 1 if ocean == "NEAR BAY" else 0
near_ocean = 1 if ocean == "NEAR OCEAN" else 0

if st.button("Predict Price"):
    data = pd.DataFrame([[longitude, latitude, housing_median_age,
                          total_rooms, total_bedrooms, population,
                          households, median_income,
                          inland, island, near_bay, near_ocean]],
                        columns=[
                            "longitude", "latitude", "housing_median_age",
                            "total_rooms", "total_bedrooms", "population",
                            "households", "median_income",
                            "ocean_proximity_INLAND",
                            "ocean_proximity_ISLAND",
                            "ocean_proximity_NEAR BAY",
                            "ocean_proximity_NEAR OCEAN"
                        ])

    prediction = model.predict(data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")