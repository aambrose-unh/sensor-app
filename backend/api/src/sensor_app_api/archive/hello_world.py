from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sensor_app_db_helper.models import SensorOutput, Sensor


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# route to read temps from database
@app.get("/read-temps")
async def read_temps():
    """
    Read temps from the database using SensorOutput sqlalchemy model.

    :return: A dictionary with the temperature data.
    """
    # Code to read temps from the database using SensorOutput sqlalchemy model

    return {"message": "temps read from the database"}


# route to write info to database
@app.post("/write-temps")
async def write_temps():
    """
    Write temps to the database using SensorOutput sqlalchemy model.

    :return: A dictionary with the temperature data.
    """
    # Code to write temps to the database using SensorOutput sqlalchemy model

    return {"message": "temps written to the database"}


# route to get sensor information from database
@app.get("/get-sensors")
async def get_sensors():
    """
    Get sensor information from the database using Sensor sqlalchemy model.

    :return: A dictionary with the sensor data.
    """
    # Code to get sensor information from the database using Sensor sqlalchemy model

    return {"message": "sensors read from the database"}
