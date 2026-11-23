import smtplib
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.send_email = os.getenv("SEND_EMAIL")


    def send_notification(self, flight_data: FlightData, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email, 
                to_addrs=self.send_email, 
                msg=message
            )
