from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Double
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime

from .database import Base


class Sensor(Base):
    __tablename__ = "sensors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(128))
    measurement_type_id: Mapped[int] = mapped_column(ForeignKey("measurement_type.id"))

    measurement_types = relationship("MeasurementType", back_populates="sensors")
    outputs = relationship("SensorOutput", back_populates="sensor")

    def __repr__(self) -> str:
        return f"Sensor(id={self.id!r}, name={self.name!r}, \
            description={self.description!r})"


class SensorOutput(Base):
    __tablename__ = "sensor_output"
    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[float] = mapped_column(Double)
    date_measured: Mapped[datetime.date]
    hour_measured: Mapped[int]
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensors.id"))

    sensor = relationship("Sensor", back_populates="outputs")

    def __repr__(self) -> str:
        return f"SensorOutput(id={self.id!r}, sensorid={self.sensorid!r}, \
                value={self.value!r}, \
                date_measured={self.date_measured!r}, hour_measured={self.hour_measured!r})"


class MeasurementType(Base):
    __tablename__ = "measurement_type"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(128))

    sensors = relationship("Sensor", back_populates="measurement_types")

    def __repr__(self) -> str:
        return f"MeasurementType(id={self.id!r}, name={self.name!r},\
              description={self.description!r})"
