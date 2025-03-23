from pydantic import BaseModel, Field
from datetime import datetime


class ScaleRequest(BaseModel):
    user_id: int = Field(gt=0, description="User's id to update")
    scale_date: datetime = Field(description="Scaling date")
    weight: float = Field(gt=40.0, lt=200.0, description="User's weight in kilograms")

    model_config = {
        "json_schema_extra": {
            "example": {
                "user_id": 3,
                "scale_date": "2025-01-15T08:30:00Z",
                "weight": 84.6,
            }
        }
    }
