from typing import List
from typing import Optional
import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import String, Double, Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class SensorOutput(Base):
    __tablename__ = "sensor_output"
    id: Mapped[int] = mapped_column(primary_key=True)
    sensorid: Mapped[int] = mapped_column(ForeignKey("sensors.id"))
    temperature: Mapped[float] = mapped_column(Double)
    humidity: Mapped[float] = mapped_column(Double)
    dateMeasured: Mapped[datetime.date]
    hourMeasured: Mapped[int]

    def __repr__(self) -> str:
        return f"SensorOutput(id={self.id!r}, sensorid={self.sensorid!r}, temperature={self.temperature!r}, \
                humidity={self.humidity!r}, dateMeasured={self.dateMeasured!r}, hourMeasured={self.hourMeasured!r})"


class Sensor(Base):
    __tablename__ = "sensors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(128))

    def __repr__(self) -> str:
        return f"Sensor(id={self.id!r}, name={self.name!r}, description={self.description!r})"
