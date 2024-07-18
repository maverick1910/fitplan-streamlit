from pydantic import BaseModel, Field
from typing import List, Dict


class MealPlan(BaseModel):
    goal: str = Field(description="The overall goal of the meal plan")
    calorie_target: str = Field(description="Daily calorie target range")
    macronutrient_breakdown: Dict[str, str] = Field(description="Breakdown of macronutrients")
    meal_frequency: str = Field(description="Recommended meal frequency")
    sample_meals: Dict[str, List[str]] = Field(description="Sample meals for each time of day")


class WorkoutPlan(BaseModel):
    goal: str = Field(description="The overall goal of the workout plan")
    frequency: str = Field(description="Recommended workout frequency")
    split: str = Field(description="Type of workout split")
    exercises: Dict[str, List[str]] = Field(description="Exercises for each workout day")


class MealWorkoutPlan(BaseModel):
    meal_plan: MealPlan
    workout_plan: WorkoutPlan
