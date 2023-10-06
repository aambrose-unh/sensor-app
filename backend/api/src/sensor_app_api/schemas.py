from pydantic import BaseModel
import datetime


class SensorOutputBase(BaseModel):
    temperature: float
    humidity: float
    dateMeasured: datetime.date
    hourMeasured: int


class SensorOutputCreate(SensorOutputBase):
    pass


class SensorOutput(SensorOutputBase):
    id: int
    sensor_id: int

    class Config:
        orm_mode = True


class SensorBase(BaseModel):
    name: str
    description: str


class SensorCreate(SensorBase):
    pass


class Sensor(SensorBase):
    id: int
    outputs: list[SensorOutput] = []

    class Config:
        orm_mode = True
