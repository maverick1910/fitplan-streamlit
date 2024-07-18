import streamlit as st


def trigger_api_request():
    print("API request triggered")


st.header('FitPlanner', divider='rainbow')
st.subheader('_An all in one customised nutrition and workout planner_  :sunglasses:')

st.markdown('''
    FitPlanner is a tool that curates a customised workout and nutrition plan for the individual based on their profile.
    
    Fill out the form below to get a curated plan for yourself 
''')

st.subheader("User Profile", divider="rainbow")

with st.form("my_form"):
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox(
        "Gender",
        ("Male", "Female", "Other"))
    height = st.number_input("Height (in cm)", min_value=1)
    weight = st.number_input("Weight (in kg)", min_value=1)
    activity_level = st.selectbox("Activity Level",
                                  ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"))
    goal = st.selectbox("Goal", ("Bulk", "Cut", "Lean Bulk", "Maintain", "Weight Loss", "Weight Gain"))
    goal_weight = st.number_input("Goal Weight (in kg)", min_value=1)
    meal_preference = st.selectbox("Meal Preference", ("Vegan", "Vegetarian", "Non-Vegetarian"))
    meal_type = st.selectbox("Type of Meal", ("Keto", "Vegan", "Balanced", "High Protein", "Low Carb", "Low Fat"))
    allergies = st.text_input("Allergies")
    medical_conditions = st.text_input("Medical Conditions")
    food_restrictions = st.text_input("Food Restrictions")
    workout_days = st.number_input("Number of days per week for workout", min_value=1, max_value=7)
    workout_location = st.selectbox("Preferred Workout Location", ("Gym", "At Home", "Outdoors"))
    workout_split = st.selectbox("Preferred Workout Split", ("Push Pull Legs", "Full Body", "Upper Lower", "Bro Split"))
    workout_experience = st.selectbox("Previous Workout Experience", ("Newbie", "Amateur", "Pro"))

    submitted = st.form_submit_button("Generate Plan")

if submitted:
    trigger_api_request()
