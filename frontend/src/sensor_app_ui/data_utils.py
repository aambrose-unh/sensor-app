# from sensor_app_api.schemas import Sensor
import requests

# Variables
api_url = "http://localhost:8000"
# TODO add api_key


# Functions
# Get all sensors
def get_sensors():
    response = requests.get(f"{api_url}/sensors")
    return response.json()


# Get sensor outputs by sensor
def get_sensor_outputs(sensor):
    response = requests.get(f"{api_url}/sensors/{sensor}/outputs")
    return response.json()
