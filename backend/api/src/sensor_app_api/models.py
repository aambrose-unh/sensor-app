from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double, Table
from sqlalchemy.orm import relationship, mapped_column, Mapped
import datetime

from .database import Base


class MeasurementType(Base):
    __tablename__ = "measurement_type"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(128))

    sensors = relationship(
        "Sensor",
        secondary="sensor_measurement_type",
        back_populates="measurement_types",
    )
    outputs = relationship(
        "SensorOutput",
        back_populates="measurement_type",
    )

    def __repr__(self) -> str:
        return f"MeasurementType(id={self.id!r}, name={self.name!r},\
              description={self.description!r})"


class Sensor(Base):
    __tablename__ = "sensors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(128))

    measurement_types = relationship(
        "MeasurementType", secondary="sensor_measurement_type", back_populates="sensors"
    )
    outputs = relationship("SensorOutput", back_populates="sensor")

    def __repr__(self) -> str:
        return f"Sensor(id={self.id!r}, name={self.name!r}, \
            description={self.description!r})"


class SensorMeasurementType(Base):
    __tablename__ = "sensor_measurement_type"
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensors.id"), primary_key=True)
    measurement_type_id: Mapped[int] = mapped_column(
        ForeignKey("measurement_type.id"), primary_key=True
    )


class SensorOutput(Base):
    __tablename__ = "sensor_output"
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float] = mapped_column(Double)
    date_measured: Mapped[datetime.date]
    hour_measured: Mapped[int]
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensors.id"))
    measurement_type_id: Mapped[int] = mapped_column(ForeignKey("measurement_type.id"))

    sensor = relationship("Sensor", back_populates="outputs")
    measurement_type = relationship("MeasurementType", back_populates="outputs")

    def __repr__(self) -> str:
        return f"SensorOutput(id={self.id!r}, sensor_id={self.sensorid!r}, \
                value={self.value!r}, \
                date_measured={self.date_measured!r}, hour_measured={self.hour_measured!r})"
