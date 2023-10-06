# from sensor_app_db_helper.models import Sensor

# s = Sensor(name="test_name", description="test_desc")
# print(s)
from sensor_app_api.schemas import (
    MeasurementTypeCreate,
    SensorCreate,
    SensorOutputCreate,
)

inst = MeasurementTypeCreate(name="test_name", description="test_desc")

print(inst.model_dump_json())
