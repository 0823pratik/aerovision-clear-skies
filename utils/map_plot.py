import pandas as pd
import folium
from folium.plugins import HeatMap

def plot_aqi_map(coord_csv):
    df = pd.read_csv(coord_csv)
    m = folium.Map(location=[28.5,77.02], zoom_start=11)
    heat_data = [[row['lat'], row['lon'], row['pm25']] for index, row in df.iterrows()]
    HeatMap(heat_data).add_to(m)
    return m._repr_html_()
