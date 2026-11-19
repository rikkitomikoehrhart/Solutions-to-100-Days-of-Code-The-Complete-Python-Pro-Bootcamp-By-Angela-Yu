import smtplib
import os
import time
from dotenv import load_dotenv
from datetime import datetime
import requests


load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
send_email = os.getenv("SEND_EMAIL")


MY_LAT = 45.57088
MY_LONG = -122.94584

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= + 5:
        return True
    else:
        return False
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=send_email,
                msg="Subject: Look Up ⬆️\n\nThe ISS is above you in the sky RIGHT NOW!"
            )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



