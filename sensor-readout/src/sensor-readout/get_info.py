#!/usr/bin/python
import sys
import random

# Ok to comment out board / adafruit_dht for testing
try:
    import board
    import adafruit_dht
except ImportError:
    print("hardware libraries not found, ok for testing, but install for production")

import os
import time
import datetime
import requests
from sensor_app_api.schemas import SensorOutputCreate

import logging

# Logging config
logger = logging.Logger("get_info")
# Create handlers
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
# Create formatters and add it to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
# Add handlers to the logger
logger.addHandler(c_handler)

logger.info("Test logger")

# VARIABLES
# Sensor app api variables
api_endpoint = os.getenv("API_ENDPOINT", "localhost:8000")
# TODO - add api key - api_key = os.getenv("API_KEY")

# Set sensor and measurement type info
sensor_id = 1
temp_measurement_type_id = 1
hum_measurement_type_id = 2

# # Hardware Info
# pinNum = board.D4  # if not using pin number 4, change here
# sensor = adafruit_dht.DHT22(pinNum)


def saveToDatabase(temperature, humidity):
    logger.info("Saving to database")

    current_datetime = datetime.datetime.now()

    # now = datetime.datetime.now()
    # # midnight = datetime.datetime.combine(now.date(), datetime.time())
    # minutes = int(
    #     ((now - midnight).seconds) / 60
    # )  # minutes after midnight, use datead$

    logger.info("Create SensorOutput instance")
    new_temp_entry = SensorOutputCreate(
        sensor_id=sensor_id,
        value=temperature,
        measurement_type_id=temp_measurement_type_id,
        date_measured=str(current_datetime),
        # hour_measured=minutes,
    )

    new_humidity_entry = SensorOutputCreate(
        sensor_id=sensor_id,
        value=humidity,
        measurement_type_id=hum_measurement_type_id,
        date_measured=str(current_datetime),
        # hour_measured=minutes,
    )

    logger.info("Saving temp output to database")
    api_url = f"http://{api_endpoint}/sensor/create/output"

    response = requests.post(api_url, json=new_temp_entry.model_dump())
    logger.info(response.text)
    logger.info("Saving humidity output to database")
    response = requests.post(api_url, json=new_humidity_entry.model_dump())
    logger.info(response.text)


# def read_info():
#     num_retries = 15
#     while num_retries > 0:
#         print(f"Number of retries remaining: {num_retries}")
#         try:
#             # Print the values to the serial port
#             temperature_c = sensor.temperature
#             temperature_f = temperature_c * (9 / 5) + 32
#             humidity = sensor.humidity
#             print(
#                 "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
#                     temperature_f, temperature_c, humidity
#                 )
#             )
#             break  # do not repeat if successful

#         except RuntimeError as error:
#             # Errors happen fairly often, DHT's are hard to read, just keep going
#             print(error.args[0])
#             time.sleep(2.0)
#             num_retries -= 1

#         except Exception as error:
#             sensor.exit()
#             raise error

#     print("Temperature: %.1f F" % temperature_f)
#     print("Humidity:    %s %%" % humidity)

#     if humidity is not None and temperature_f is not None:
#         return saveToDatabase(temperature_f, humidity)  # success, save the readings
#     else:
#         print("Failed to get reading. Try again!")
#         sys.exit(1)


def test_read_info(num_data_points=10):
    for i in range(num_data_points):
        temperature_f = random.randint(0, 100)
        humidity = random.randint(0, 100)

        print("Temperature: %.1f F" % temperature_f)
        print("Humidity:    %s %%" % humidity)

        saveToDatabase(temperature_f, humidity)  # success, save the readings


if __name__ == "__main__":
    # read_info()  # get the readings
    test_read_info()
