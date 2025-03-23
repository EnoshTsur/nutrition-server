from pydantic import BaseModel, Field, EmailStr
from app.models.gender import Gender
from app.models.activity_level import ActivityLevel
from app.models.diet_phase import DietPhase


class UserRequest(BaseModel):
    given_name: str = Field(min_length=3)
    family_name: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=8)  # Should be min 8 chars for security
    weight: float = Field(gt=40.0, lt=200.0)
    height: int = Field(gt=130, lt=220)
    age: int = Field(gt=10, lt=120)
    gender: Gender
    activity_level: ActivityLevel
    diet_phase: DietPhase

    model_config = {
        "json_schema_extra": {
            "example": {
                "given_name": "Enosh",
                "family_name": "Tsur",
                "email": "enoshh12@example.com",
                "password": "abcd1234!K",
                "weight": 85.5,
                "height": 175,
                "age": 34,
                "gender": "MALE",
                "activity_level": "EXTRA_ACTIVE",
                "diet_phase": "BULK",
            }
        }
    }
