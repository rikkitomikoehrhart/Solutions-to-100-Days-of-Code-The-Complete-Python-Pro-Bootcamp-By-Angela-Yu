import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
GRAPH_ID = "graph1"
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
PIXEL_UPDATE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/{formatted_today}"


user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# USER IS CREATED
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Test Graph",
    "unit": "minute",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# GRAPH IS CREATED
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)


pixel_data = {
    "date": formatted_today,
    "quantity": "62",
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)

update_data = {
    "quantity": "72"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_data, headers=headers)


response = requests.delete(url=PIXEL_UPDATE_ENDPOINT, headers=headers)
print(response.text)

