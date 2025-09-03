🌾 IFFCO Urea Usage Optimization Dashboard

An AI-powered, farmer-centric dashboard that predicts the optimal Urea fertilizer usage and provides actionable insights for better crop management.

Built using Machine Learning, Streamlit, and OpenWeather API, this tool helps farmers and agri-organizations make data-driven decisions while reducing costs and improving sustainability.

🚀 Features

✅ AI-based Prediction – Recommends the exact urea requirement (kg) based on:

Crop type

Land area (ha)

Soil fertility

Growth stage

Region

✅ Real-time Weather Integration – Uses OpenWeather API to fetch:

🌡️ Temperature

💧 Humidity

🌧️ Rainfall
for major agricultural states (Punjab, Haryana, UP, Bihar).

✅ Interactive Dashboard – Built with Streamlit, featuring:

Clean, farmer-friendly UI

Sidebar for inputs

Instant fertilizer recommendations

✅ Scalable & Deployable – Easily deployable on Streamlit Community Cloud or any cloud server.

📊 Tech Stack

Python (Data processing, ML model training)

Scikit-learn (ML model)

Pandas, NumPy (Data wrangling)

Matplotlib (Visualization – optional)

Streamlit (Dashboard UI)

OpenWeather API (Weather data integration)

📂 Project Structure
IFFCO_Urea_App/
│── app.py                 # Main Streamlit app
│── urea_model.pkl         # Trained ML model
│── label_encoders.pkl     # Encoders for categorical features
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation