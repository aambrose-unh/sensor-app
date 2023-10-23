import streamlit as st
import numpy as np
import pandas as pd
from data_utils import get_sensors, get_sensor_outputs

st.title('Sensor App')

sensors = get_sensors()

# Select sensor from drop down
selected_sensor = st.selectbox(
    "Select a sensor", sensors
)

@st.cache_data
sensor_outputs = get_sensor_outputs(sensors[0].id)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))


# Show raw data below chart
st.dataframe(sensor_outputs)