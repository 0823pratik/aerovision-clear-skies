# aerovision-clear-skies
# AeroVision-GGM 🌫️📍
**AI-GIS Dashboard for Predictive Air Quality Mapping in Gurugram**  
_An entry for the Google-backed Clear Skies Challenge 2025_

---

## 🚀 Overview

AeroVision-GGM is a smart, interactive platform for forecasting and visualizing air pollution (PM2.5) in Gurugram, Haryana.  
The system combines **LSTM-based time-series forecasting** with **GIS-based heatmaps** to empower policymakers, citizens, and urban planners with actionable insights.

### 🎯 Key Features
- 🔮 **AI-Powered AQI Prediction** (6 to 24 hours)
- 🗺️ **Live Geospatial Heatmap** of PM2.5 values
- 🧠 **LSTM Neural Network Model** for PM2.5 forecasting
- 🌐 **Streamlit Web Dashboard** for ease of use

---

## 📸 Demo Preview

📦 <img width="1919" height="862" alt="image" src="https://github.com/user-attachments/assets/2f4e0930-643a-4552-8aeb-16ab91ae6d0f" />


---

## 🧠 Project Structure
<img width="744" height="516" alt="System Architecture – AeroVision-GGM (Smart Cities AQI Platform) - visual selection" src="https://github.com/user-attachments/assets/8af3332b-218d-4330-a669-9e7d27aa3653" />

```
aerovision/
│
├── app.py                  # Main Streamlit app
│
├── data/
│   ├── aqi_data.csv        # Hourly PM2.5 dataset
│   └── sample_coords.csv   # Coordinates + PM2.5 for heatmap
│
├── utils/
│   ├── model.py            # LSTM forecasting logic
│   └── map_plot.py         # Folium heatmap rendering
│
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions
```


---

## ⚙️ Tech Stack

| Category        | Tools/Frameworks                     |
|----------------|--------------------------------------|
| Web Framework  | Streamlit                            |
| AI/ML          | TensorFlow, Keras (LSTM)             |
| Data Handling  | Pandas, NumPy                        |
| Geospatial     | Folium, Leaflet.js, OpenStreetMap    |
| Visualization  | Streamlit Charts, Matplotlib         |

---

## 🗺️ How It Works

1. `aqi_data.csv` is loaded to get past hourly PM2.5 readings
2. The LSTM model (`utils/model.py`) forecasts future values
3. `sample_coords.csv` provides latitude/longitude/PM2.5 points
4. A **Folium heatmap** shows current spatial distribution
5. Everything is combined into a **Streamlit dashboard** (`app.py`)

---

## 📂 Sample Data

### `data/aqi_data.csv`
```csv
timestamp,pm25
2025-07-13 00:00,110
2025-07-13 01:00,112
...

### `data/sample_coords.csv`
```csv
lat,lon,pm25
28.4595,77.0266,138
28.4648,77.0291,125
...
### `How to Run Locally`
git clone https://github.com/0823pratik/aerovision-clear-skies.git
cd aerovision-clear-skies
pip install -r requirements.txt
python streamlit run app.py

 ### `Credits`
This project was submitted to the Clear Skies Challenge 2025, backed by Google, under:

🏙️ Track: Smart Cities
🏢 City: Gurugram, Haryana
📌 Problem Statement 2: Predictive AI for Air Quality Management

### `Contact`
Pratik Raj
IIT Tirupati
pratik08raj@gmail.com
ee23b042@iittp.ac.in



