from dotenv import load_dotenv
import os
import requests

load_dotenv()


SHEETY_URL = os.getenv("SHEETY_URL")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")

SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }

        requests.put(url=f"{SHEETY_URL}/{row_id}", json=new_data, headers=SHEETY_HEADERS)