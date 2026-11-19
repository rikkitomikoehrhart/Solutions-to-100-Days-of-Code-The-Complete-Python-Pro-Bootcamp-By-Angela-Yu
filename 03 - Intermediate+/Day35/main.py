import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
MY_LAT = 45.57088
MY_LONG = -122.94584

OWN_Endpoint = os.getenv("OWN_Endpoint")
OWN_API_KEY = os.getenv("OWN_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_num = os.getenv("FROM_NUMBER")
to_num = os.getenv("TO_NUMBER")


weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWN_API_KEY,
    "cnt": 4,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella", from_=from_num, to=to_num)
