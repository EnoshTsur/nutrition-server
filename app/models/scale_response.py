from pydantic import BaseModel, Field
from datetime import datetime


class ScaleResponse(BaseModel):
    id: int
    user_id: int = Field(description="User ID this scale report belongs to")
    scale_date: datetime = Field(description="Date when the measurement was taken")
    weight: float = Field(description="User's weight in kilograms")
    created_at: datetime = Field(
        description="When this record was created in the system"
    )

    model_config = {
        "from_attributes": True,  # Enables conversion from SQLAlchemy model
        "json_schema_extra": {
            "example": {
                "id": 1,
                "user_id": 42,
                "scale_date": "2025-01-15T08:30:00Z",
                "weight": 75.5,
                "created_at": "2025-01-15T08:35:12Z",
            }
        },
    }
