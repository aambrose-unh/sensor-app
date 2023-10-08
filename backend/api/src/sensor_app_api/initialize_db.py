from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import datetime

from sensor_app_api import crud, models, schemas
from sensor_app_api.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    with Session(bind=engine) as db:
        # Create dht22 sensor
        crud.create_sensor(
            db=db,
            sensor=schemas.SensorCreate(
                name="DHT22", description="Temperature and Humidity sensor"
            ),
        )
        # Create measurement types
        crud.create_measurement_type(
            db,
            measurement_type=schemas.MeasurementTypeCreate(
                name="Temperature", description="Temperature"
            ),
        )
        crud.create_measurement_type(
            db,
            measurement_type=schemas.MeasurementTypeCreate(
                name="Humidity", description="Humidity"
            ),
        )

        # Look up sensor id and measurement id by name
        sensor = crud.get_sensor_by_name(db, name="DHT22")
        measurement_type = crud.get_measurement_type_by_name(db, name="Temperature")
        crud.create_sensor_measurement_type(
            db,
            schemas.SensorMeasurementType(
                sensor_id=sensor.id, measurement_type_id=measurement_type.id
            ),
        )

        sensor = crud.get_sensor_by_name(db, name="DHT22")
        measurement_type = crud.get_measurement_type_by_name(db, name="Humidity")
        crud.create_sensor_measurement_type(
            db,
            schemas.SensorMeasurementType(
                sensor_id=sensor.id, measurement_type_id=measurement_type.id
            ),
        )


if __name__ == "__main__":
    init_db()
