import streamlit as st
import numpy as np
import pandas as pd
from data_utils import get_sensors, get_sensor_outputs

st.title('Sensor App')

# Load sensors
sensors = get_sensors()

# Select sensor from drop down in a sidebar
selected_sensor = st.sidebar.selectbox(
    "Select a sensor", sensors
)

# Load Sensor Outputs
@st.cache_data
sensor_outputs = get_sensor_outputs(selected_sensor.id)



