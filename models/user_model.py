from pydantic import BaseModel


class UserInput(BaseModel):
    age: int
    gender: str = "N/A"
    height: int = 0
    weight: float = 0
    activity_level: str = "N/A"
    goal: str = "N/A"
    goal_weight: float = 0
    meal_preference: str = "N/A"
    meal_type: str = "N/A"
    allergies: str = "N/A"
    medical_conditions: str = "N/A"
    food_restrictions: str = "N/A"
    workout_days: int = 0
    workout_location: str = "N/A"
    workout_split: str = "N/A"
    workout_experience: str = "N/A"
