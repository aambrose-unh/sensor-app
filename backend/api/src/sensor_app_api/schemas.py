from pydantic import BaseModel, field_serializer
import datetime


class SensorOutputBase(BaseModel):
    value: float
    sensor_id: int
    measurement_type_id: int
    date_measured: datetime.date
    hour_measured: int

    @field_serializer("date_measured")
    def serialize_dt(self, date_measured: datetime.date, _info):
        return str(date_measured)


class SensorOutputCreate(SensorOutputBase):
    pass


class SensorOutput(SensorOutputBase):
    id: int

    class Config:
        orm_mode = True


class SensorBase(BaseModel):
    name: str
    description: str
    measurement_type_id: int


class SensorCreate(SensorBase):
    pass


class Sensor(SensorBase):
    id: int
    outputs: list[SensorOutput] = []

    class Config:
        orm_mode = True


class MeasurementTypeBase(BaseModel):
    name: str
    description: str


class MeasurementTypeCreate(MeasurementTypeBase):
    pass


class MeasurementType(MeasurementTypeBase):
    id: int
    sensors: list[Sensor] = []

    class Config:
        orm_mode = True
