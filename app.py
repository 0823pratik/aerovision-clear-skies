import streamlit as st
import pandas as pd
from utils.map_plot import plot_aqi_map
from model.lstm_predictor import predict_aqi

st.set_page_config(layout="wide")
st.title("🌍 AeroVision - Smart City AQI Dashboard")

st.sidebar.title("Select Forecast Duration")
hours = st.sidebar.slider("Forecast Next Hours", 1, 24, 12)

st.sidebar.markdown("#### 📍 City: Gurugram")

# Load historical AQI data
aqi_data = pd.read_csv("data/aqi_data.csv")

# Predict using LSTM
predicted_aqi = predict_aqi(aqi_data["pm25"].values, forecast_hours=hours)

st.subheader("📊 Forecasted AQI (Next {} hours)".format(hours))
st.line_chart(predicted_aqi)

# Show geospatial AQI map
st.subheader("🗺️ Real-Time AQI Heatmap (Coordinates)")
aqi_map = plot_aqi_map("data/sample_coords.csv")
st.components.v1.html(aqi_map, height=500, scrolling=True)
