import os
from dotenv import load_dotenv
import requests
from exercise import Exercise

load_dotenv()

USER_ID = os.getenv("USER_ID")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
EXERCISE_URL = f"{BASE_URL}/v1/nutrition/natural/exercise"
SHEETY_URL = os.getenv("SHEETY_URL")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

APP_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

SHEETY_HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}


using_app = True

while using_app:
    query = input("What workout did you do today? (50 characters or less or type `exit` to exit): ")

    if query.lower() == "exit":
        using_app = False
        break

    user_params = {
        "query": query
    }

    # Get Exercise Data
    response = requests.post(url=EXERCISE_URL, json=user_params, headers=APP_HEADERS)
    data = response.json()
    exercise_data = data["exercises"][0]

    # Create Exercise objects 
    workout = Exercise(exercise_data)

    # Add workout to google sheets
    workout_params = {
        "workout": {
            "date": workout.date,
            "time": workout.time,
            "exercise": workout.exercise,
            "duration": workout.duration,
            "calories": workout.calories,
        }
    }

    response = requests.post(url=SHEETY_URL, json=workout_params, headers=SHEETY_HEADERS)

    print("\n\n")