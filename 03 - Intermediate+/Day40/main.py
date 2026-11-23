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
message = ""

sheet_data = data_manager.get_destination_data()
customer_data = data_manager.get_customer_emails()
customer_email_list = [row["email:"] for row in customer_data] 

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")


for city in sheet_data:
    flights = flight_search.check_flights("LHR", city["iataCode"], tomorrow, six_months_from_today)
    cheapest_flight = find_cheapest_flight(data=flights, return_date=six_months_from_today)

    if cheapest_flight.price != "N/A" and cheapest_flight.price < city["lowestPrice"]:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only ${cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only ${cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}," \
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        pprint(f"Lower price flight found to {city["city"]}!")
        data_manager.update_lowest_price(city["id"], cheapest_flight.price)
        notification_manager.send_notification(cheapest_flight, message)

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {city["city"]}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights("LHR", city["iataCode"], tomorrow, six_months_from_today, is_direct=False)

        cheapest_flight = find_cheapest_flight(stopover_flights, 
        return_date=six_months_from_today.strftime("%Y-%m-%d"))