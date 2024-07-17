def fetch_template_data(user_data):
    template = f"""
        Curate a customized workout plan and nutrition plan for the individual with the following profile:
            Age : {user_data['age']}
            Gender : {user_data['gender']}
            Height : {user_data['height']}
            Weight : {user_data['weight']}
            Activity Level : {user_data['activity_level']}
            Goal (Bulk / Cut / Lean Bulk etc) : {user_data['goal']}
            Goal Weight : {user_data['goal_weight']}
            Meal Preference : {user_data['meal_preference']}
            Type of Meal ( Keto / Vegan / Vegetarian / Non-Vegetarian, etc ) : {user_data['meal_type']}
            Allergies : {user_data['allergies']}
            Medical Conditions : {user_data['medical_conditions']}
            Food Restrictions : {user_data['food_restrictions']}
            Number of days per week for workout : {user_data['workout_days']}
            Preferred Workout Location (Gym, At Home , etc) : {user_data['workout_location']}
            Preferred Workout Split (Push Pull Legs, Full Body, etc) : {user_data['workout_split']}
            Previous Workout Experience (Newbie / Amateur / Pro)  : {user_data['workout_experience']}
        
        If any information is termed N/A , it means the user has not provided the information, provide plan accordingly.
        In Case of any missing information, please provide the necessary details.
        
        Answer: A curated meal plan and workout plan is created according to the profile.
        
        Meal Plan : 
        Workout Plan :
        Links to the recipes and workout videos are provided at every stage
            
    """
    return template
