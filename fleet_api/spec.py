from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin

spec = APISpec(
    title="Fleet Management API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin()],
)

spec.components.schema(
    "TaxiModel",
    {
        "properties": {
            "id": {"type": "integer", "format": "int64"},
            "plate": {"type": "string"},
        }
    },
)

spec.components.schema(
    "LocationsModel",
    {
        "properties": {
            "id": {"type": "integer", "format": "int64"},
            "plate": {"type": "string"},
            "timestamp": {"type": "string", "format": "date-time"},
            "lat": {"type": "string"},
            "lon": {"type": "string"},
        }
    },
)
