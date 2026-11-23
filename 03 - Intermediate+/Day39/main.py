from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


sheet_data = data_manager.get_destination_data()


tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")


for city in sheet_data:
    flights = flight_search.check_flights("LHR", city["iataCode"], tomorrow, six_months_from_today)
    cheapest_flight = find_cheapest_flight(data=flights, return_date=six_months_from_today)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < city["lowestPrice"]:
        pprint(f"Lower price flight found to {city["city"]}!")
        data_manager.update_lowest_price(city["id"], cheapest_flight.price)
        notification_manager.send_notification(cheapest_flight)

