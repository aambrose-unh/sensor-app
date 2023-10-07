#!/usr/bin/python
import sys
import random

# import board
# import adafruit_dht

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

# databaseUsername = os.getenv("DB_USER")
# databasePassword = os.getenv("DB_PASSWD")
# databaseName = "sensor_db"
api_endpoint = os.getenv("API_ENDPOINT", "localhost:8000")
# api_key = os.getenv("API_KEY")


def saveToDatabase(temperature, humidity):
    logger.info("Saving to database")

    # connection_uri = f"mysql+pymysql://{databaseUsername}:{databasePassword}@localhost/{databaseName}"
    # engine = create_engine(connection_uri, echo=True)
    current_date = datetime.datetime.now().date()

    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    minutes = int(
        ((now - midnight).seconds) / 60
    )  # minutes after midnight, use datead$

    logger.info("Create SensorOutput instance")
    new_temp_entry = SensorOutputCreate(
        sensor_id=2,
        value=temperature,
        date_measured=str(current_date),
        hour_measured=minutes,
    )

    new_humidity_entry = SensorOutputCreate(
        sensor_id=2,
        value=humidity,
        date_measured=str(current_date),
        hour_measured=minutes,
    )

    logger.info("Save temp output to database")
    api_url = f"http://{api_endpoint}/sensor/create/output"
    response = requests.post(api_url, json=new_temp_entry.model_dump())
    logger.info(response.text)
    logger.info("Save humidity output to database")
    response = requests.post(api_url, json=new_humidity_entry.model_dump())
    logger.info(response.text)

    logger.info("Saved temperature")


def readInfo():
    temperature_f = random.randint(0, 100)
    humidity = random.randint(0, 100)

    # num_retries = 15
    # while num_retries > 0:
    #     print(f"Number of retries remaining: {num_retries}")
    #     try:
    #         # Print the values to the serial port
    #         temperature_c = sensor.temperature
    #         temperature_f = temperature_c * (9 / 5) + 32
    #         humidity = sensor.humidity
    #         print(
    #             "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
    #                 temperature_f, temperature_c, humidity
    #             )
    #         )
    #         break  # do not repeat if successful

    #     except RuntimeError as error:
    #         # Errors happen fairly often, DHT's are hard to read, just keep going
    #         print(error.args[0])
    #         time.sleep(2.0)
    #         num_retries -= 1

    #     except Exception as error:
    #         sensor.exit()
    #         raise error

    print("Temperature: %.1f C" % temperature_f)
    print("Humidity:    %s %%" % humidity)

    if humidity is not None and temperature_f is not None:
        return saveToDatabase(temperature_f, humidity)  # success, save the readings
    else:
        print("Failed to get reading. Try again!")
        sys.exit(1)


if __name__ == "__main__":
    status = readInfo()  # get the readings
