from sqlalchemy.orm import Session
import datetime

from . import models, schemas


def get_sensor(db: Session, sensor_id: int):
    return db.query(models.Sensor).filter(models.Sensor.id == sensor_id).first()


def get_sensor_by_name(db: Session, name: str):
    return db.query(models.Sensor).filter(models.Sensor.name == name).first()


def get_sensors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Sensor).offset(skip).limit(limit).all()


def get_measurement_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MeasurementType).offset(skip).limit(limit).all()


def get_measurement_type_by_name(db: Session, name: str):
    return (
        db.query(models.MeasurementType)
        .filter(models.MeasurementType.name == name)
        .first()
    )


def create_sensor(db: Session, sensor: schemas.SensorCreate):
    db_sensor = models.Sensor(
        name=sensor.name,
        description=sensor.description,
    )
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


def create_measurement_type(
    db: Session, measurement_type: schemas.MeasurementTypeCreate
):
    db_measurement_type = models.MeasurementType(
        name=measurement_type.name, description=measurement_type.description
    )
    db.add(db_measurement_type)
    db.commit()
    db.refresh(db_measurement_type)
    return db_measurement_type


def get_outputs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SensorOutput).offset(skip).limit(limit).all()


def get_outputs_by_sensor_id(db: Session, sensor_id: int):
    return (
        db.query(models.SensorOutput)
        .filter(models.SensorOutput.sensor_id == sensor_id)
        .all()
    )


def create_sensor_measurement_type(
    db: Session, sensor_measurement_type: schemas.SensorMeasurementType
):
    db_sensor_measurement_type = models.SensorMeasurementType(
        sensor_id=sensor_measurement_type.sensor_id,
        measurement_type_id=sensor_measurement_type.measurement_type_id,
    )
    db.add(db_sensor_measurement_type)
    db.commit()
    db.refresh(db_sensor_measurement_type)
    return db_sensor_measurement_type


def get_outputs_by_sensor_name(db: Session, sensor_name: str):
    return (
        db.query(models.SensorOutput)
        .filter(models.SensorOutput.sensor.name == sensor_name)
        .all()
    )


def get_outputs_by_sensor_id_and_date(db: Session, sensor_id: int, date: datetime.date):
    return (
        db.query(models.SensorOutput)
        .filter(
            models.SensorOutput.sensor_id == sensor_id,
            models.SensorOutput.date_measured == date,
        )
        .all()
    )


def get_outputs_by_sensor_id_and_date_range(
    db: Session, sensor_id: int, start_date: datetime.date, end_date: datetime.date
):
    return (
        db.query(models.SensorOutput)
        .filter(
            models.SensorOutput.sensor_id == sensor_id,
            models.SensorOutput.date_measured >= start_date,
            models.SensorOutput.date_measured <= end_date,
        )
        .all()
    )


def get_outputs_by_measurement_type_id(db: Session, measurement_type_id: int):
    return (
        db.query(models.SensorOutput)
        .filter(models.SensorOutput.sensor.measurement_type_id == measurement_type_id)
        .all()
    )


def create_sensor_output(db: Session, sensor_output: schemas.SensorOutputCreate):
    db_sensor_output = models.SensorOutput(
        **sensor_output.model_dump(),
    )
    db.add(db_sensor_output)
    db.commit()
    db.refresh(db_sensor_output)
    return db_sensor_output
