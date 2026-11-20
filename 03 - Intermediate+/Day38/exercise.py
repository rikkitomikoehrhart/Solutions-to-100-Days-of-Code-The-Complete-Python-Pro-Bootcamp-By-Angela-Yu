from datetime import datetime

class Exercise:

    def __init__(self, exercise_data):
        self.date = datetime.now().strftime("%m/%d/%Y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.exercise = exercise_data["name"].title()
        self.duration = exercise_data["duration_min"]
        self.calories = exercise_data["nf_calories"]