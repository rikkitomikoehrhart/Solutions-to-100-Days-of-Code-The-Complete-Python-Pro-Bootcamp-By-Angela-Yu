from dotenv import load_dotenv
import os
import requests

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BASE_URL = f"{os.getenv("BASE_URL")}/v1/flights/search"

APP_HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self._api_key = API_KEY


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        query_params = {
            "engine": "google_flights",
            "api_key": self._api_key,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
        }

        if is_direct:
            query_params["stops"] = "1"

        response = requests.get(url=BASE_URL, params=query_params, headers=APP_HEADERS)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None

        return data