from pydantic import BaseModel
from app.models.gender import Gender
from app.models.activity_level import ActivityLevel
from app.models.diet_phase import DietPhase


class UserResponse(BaseModel):
    id: int
    given_name: str
    family_name: str
    email: str
    weight: float
    height: int
    age: int
    gender: Gender
    activity_level: ActivityLevel
    diet_phase: DietPhase
    tdee: float

    class Config:
        from_attributes = True
