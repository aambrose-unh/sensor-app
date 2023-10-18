import streamlit as st
import numpy as np
import pandas as pd
from sensor_app_ui.data_utils import get_sensors, get_sensor_outputs

st.title("Sensor App")

# Load sensors
sensors = get_sensors()

# Select sensor from drop down in a sidebar
selected_sensor = st.sidebar.selectbox("Select a sensor", sensors["name"])
selected_sensor_id = int(sensors[sensors["name"] == selected_sensor]["id"].values[0])


# Load Sensor Outputs
@st.cache_data
def load_sensor_outputs(sensor):
    return get_sensor_outputs(sensor=sensor)


df_sensor_outputs = load_sensor_outputs(selected_sensor_id)

st.write(df_sensor_outputs)

st.line_chart(df_sensor_outputs[["value"]])
