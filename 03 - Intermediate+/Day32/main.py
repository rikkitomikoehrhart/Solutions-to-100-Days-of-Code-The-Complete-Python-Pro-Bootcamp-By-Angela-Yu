import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
send_email = os.getenv("SEND_EMAIL")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=send_email, msg=f"Subject:Thursday Motivation!\n\n{quote}")


