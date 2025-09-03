import streamlit as st
import pickle
import pandas as pd
import requests

# ---------------------------
# Load Model and Encoders
# ---------------------------
with open("urea_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# ---------------------------
# Weather API Function
# ---------------------------
API_KEY = "728dad02e5e432e5db371a47cd8709cf"   # replace with your OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
    else:
        return {"Temperature": "N/A", "Humidity": "N/A", "Weather": "N/A"}

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="IFFCO Urea Optimizer", page_icon="🌱", layout="wide")

st.title("🌾 IFFCO Urea Usage Optimization Dashboard")
st.markdown("A farmer-centric tool to predict **optimal Urea requirement** with **real-time weather insights**.")

# ---------------------------
# Sidebar Inputs
# ---------------------------
st.sidebar.header("⚙️ Input Parameters")

# Region-wise cities
state_cities = {
    "Punjab": ["Ludhiana", "Amritsar", "Patiala"],
    "Haryana": ["Karnal", "Hisar", "Rohtak"],
    "Uttar Pradesh": ["Lucknow", "Varanasi", "Kanpur"],
    "Bihar": ["Patna", "Gaya", "Muzaffarpur"]
}

state = st.sidebar.selectbox("Select State", list(state_cities.keys()))
city = st.sidebar.selectbox("Select City", state_cities[state])

crop = st.sidebar.selectbox("Crop", label_encoders["Crop"].classes_)
land_area = st.sidebar.number_input("Land Area (ha)", min_value=0.1, step=0.1)
fertility = st.sidebar.selectbox("Soil Fertility", label_encoders["Soil_Fertility"].classes_)
stage = st.sidebar.selectbox("Growth Stage", label_encoders["Growth_Stage"].classes_)
region = st.sidebar.selectbox("Region", label_encoders["Region"].classes_)

# Encode user inputs
encoded = {
    "Crop": label_encoders["Crop"].transform([crop])[0],
    "Land_Area_ha": land_area,
    "Soil_Fertility": label_encoders["Soil_Fertility"].transform([fertility])[0],
    "Growth_Stage": label_encoders["Growth_Stage"].transform([stage])[0],
    "Region": label_encoders["Region"].transform([region])[0],
}

input_df = pd.DataFrame([encoded])

# ---------------------------
# Prediction
# ---------------------------
prediction = model.predict(input_df)[0]

# ---------------------------
# Weather Data
# ---------------------------
weather = get_weather(city)

# ---------------------------
# Display Results
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌱 Urea Prediction")
    st.metric(label="Recommended Urea (kg)", value=f"{prediction:.2f} kg")

with col2:
    st.subheader(f"🌦️ Weather in {city}")
    st.metric(label="Temperature", value=f"{weather['Temperature']} °C")
    st.metric(label="Humidity", value=f"{weather['Humidity']} %")
    st.write(f"**Condition:** {weather['Weather'].title()}")

st.success(f"✅ Prediction for {crop} in {city}, {state} completed!")
