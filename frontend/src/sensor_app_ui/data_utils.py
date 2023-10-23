# from sensor_app_api.schemas import Sensor
import requests
import pandas as pd

# Variables
api_url = "http://localhost:8000"
# TODO add api_key


# Functions
# Get all sensors
def get_sensors():
    response = requests.get(f"{api_url}/sensors")
    sensors = response.json()

    # Create DataFrame of sensors
    # df_sensors = pd.DataFrame(sensors)

    return pd.DataFrame(sensors)


# Get sensor outputs by sensor
def get_sensor_outputs(sensor):
    response = requests.get(f"{api_url}/sensor/{sensor}/output")
    sensor_outputs = response.json()

    # Create DataFrame of sensor outputs
    df_sensor_outputs = pd.DataFrame(sensor_outputs)
    df_sensor_outputs.set_index("date_measured")

    return df_sensor_outputs
