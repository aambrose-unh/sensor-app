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

    outputs = relationship("SensorOutput", back_populates="sensor")

    def __repr__(self) -> str:
        return f"Sensor(id={self.id!r}, name={self.name!r}, description={self.description!r})"


class SensorOutput(Base):
    __tablename__ = "sensor_output"
    id: Mapped[int] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column(Double)
    humidity: Mapped[float] = mapped_column(Double)
    dateMeasured: Mapped[datetime.date]
    hourMeasured: Mapped[int]
    sensor_id: Mapped[int] = mapped_column(ForeignKey("sensors.id"))

    sensor = relationship("Sensor", back_populates="outputs")

    def __repr__(self) -> str:
        return f"SensorOutput(id={self.id!r}, sensorid={self.sensorid!r}, temperature={self.temperature!r}, \
                humidity={self.humidity!r}, dateMeasured={self.dateMeasured!r}, hourMeasured={self.hourMeasured!r})"
