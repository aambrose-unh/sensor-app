from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import datetime

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sensor/create", response_model=schemas.Sensor)
def create_sensor(sensor: schemas.SensorCreate, db: Session = Depends(get_db)):
    db_sensor = crud.create_sensor(db, sensor)
    return db_sensor


@app.get("/sensor/{sensor_id}", response_model=schemas.Sensor)
def get_sensor(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor = crud.get_sensor(db, sensor_id)
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor not found")
    return db_sensor


@app.post("/sensor/create/output", response_model=schemas.SensorOutput)
def create_sensor_output(
    sensor_output: schemas.SensorOutputCreate, db: Session = Depends(get_db)
):
    db_sensor_output = crud.create_sensor_output(db, sensor_output)
    return db_sensor_output


@app.get("/sensor/{sensor_id}/output", response_model=list[schemas.SensorOutput])
def get_sensor_outputs(sensor_id: int, db: Session = Depends(get_db)):
    db_sensor_outputs = crud.get_outputs_by_sensor_id(db, sensor_id)
    return db_sensor_outputs


@app.get("/sensor/{sensor_id}/output/{date}", response_model=list[schemas.SensorOutput])
def get_sensor_outputs_by_date(
    sensor_id: int, date: datetime.date, db: Session = Depends(get_db)
):
    db_sensor_outputs = crud.get_outputs_by_sensor_id_and_date(db, sensor_id, date)
    return db_sensor_outputs


@app.get(
    "/sensor/{sensor_id}/output/range/{start_date}/{end_date}",
    response_model=list[schemas.SensorOutput],
)
def get_sensor_outputs_by_date_range(
    sensor_id: int,
    start_date: datetime.date,
    end_date: datetime.date,
    db: Session = Depends(get_db),
):
    db_sensor_outputs = crud.get_outputs_by_sensor_id_and_date_range(
        db, sensor_id, start_date, end_date
    )
    return db_sensor_outputs


@app.get(
    "/sensor/{sensor_id}/output/type/{measurement_type_id}",
    response_model=list[schemas.SensorOutput],
)
def get_sensor_outputs_by_measurement_type_id(
    sensor_id: int, measurement_type_id: int, db: Session = Depends(get_db)
):
    db_sensor_outputs = crud.get_outputs_by_measurement_type_id(db, measurement_type_id)
    return db_sensor_outputs


@app.post("/measurement-type/create", response_model=schemas.MeasurementType)
def create_measurement_type(
    measurement_type: schemas.MeasurementTypeCreate, db: Session = Depends(get_db)
):
    db_measurement_type = crud.create_measurement_type(db, measurement_type)
    return db_measurement_type


@app.get(
    "/measurement-type/{measurement_type_id}", response_model=schemas.MeasurementType
)
def get_measurement_type(measurement_type_id: int, db: Session = Depends(get_db)):
    db_measurement_type = crud.get_measurement_type(db, measurement_type_id)
    if db_measurement_type is None:
        raise HTTPException(status_code=404, detail="Measurement type not found")
    return db_measurement_type


@app.get("/measurement-type", response_model=list[schemas.MeasurementType])
def get_measurement_types(db: Session = Depends(get_db)):
    db_measurement_types = crud.get_measurement_types(db)
    return db_measurement_types


@app.get("/sensors/", response_model=list[schemas.Sensor])
def get_sensors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_sensors = crud.get_sensors(db, skip=skip, limit=limit)
    return db_sensors


@app.get("/outputs/", response_model=list[schemas.SensorOutput])
def get_outputs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_outputs = crud.get_outputs(db, skip=skip, limit=limit)
    return db_outputs


# TODO Implement alembic for migrations
