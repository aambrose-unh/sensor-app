#!/usr/bin/python
import sys
import random

import os
import time
import pymysql as mdb
import pymysql.cursors
import datetime
from sqlalchemy import create_engine, text
from sqlalchemy import insert
from sensor_app_db.models import SensorOutput


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

databaseUsername = os.getenv("DB_USER")
databasePassword = os.getenv("DB_PASSWD")
databaseName = "sensor_db"  # do not change unless you named the Wordpress database with some other name


def saveToDatabase(temperature, humidity):
    logger.info("Saving to database")

    connection_uri = f"mysql+pymysql://{databaseUsername}:{databasePassword}@localhost/{databaseName}"
    engine = create_engine(connection_uri, echo=True)
    currentDate = datetime.datetime.now().date()

    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    minutes = ((now - midnight).seconds) / 60  # minutes after midnight, use datead$

    logger.info("Create db connection")
    # with engine.connect() as con:
    # cur = con.cursor()
    # q = "INSERT INTO temperatures (temperature,humidity, dateMeasured, hourMeasured) VALUES (%s, %s, %s, %s)"
    # logger.info(f"Inserting record {q}")
    # v = (temperature, humidity, str(currentDate), minutes)
    # logger.info(f"Values: {v}")
    # con.execute(q, v)
    new_entry = SensorOutput(
        sensorid=1,
        temperature=temperature,
        humidity=humidity,
        dateMeasured=str(currentDate),
        hourMeasured=minutes,
    )

    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_entry)
    session.commit()

    print("Saved temperature")
    return "true"


def readInfo():
    temperature_f = random.randint(0, 100)
    humidity = random.randint(0, 100)

    print("Temperature: %.1f C" % temperature_f)
    print("Humidity:    %s %%" % humidity)

    if humidity is not None and temperature_f is not None:
        return saveToDatabase(temperature_f, humidity)  # success, save the readings
    else:
        print("Failed to get reading. Try again!")
        sys.exit(1)


if __name__ == "__main__":
    status = readInfo()  # get the readings
