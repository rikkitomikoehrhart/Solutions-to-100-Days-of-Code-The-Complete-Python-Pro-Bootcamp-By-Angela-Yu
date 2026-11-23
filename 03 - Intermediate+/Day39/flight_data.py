class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("There is no flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    first_flight = all_flights[0]
    first_flight_price = int(first_flight["price"])
    first_flight_origin = first_flight["flights"][0]["departure_airport"]["id"]
    first_flight_destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    first_flight_out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    cheapest_flight = FlightData(price=first_flight_price, origin_airport=first_flight_origin, destination_airport=first_flight_destination, out_date=first_flight_out_date, return_date=return_date)

    for flight in all_flights:
       if int(flight["price"]) < cheapest_flight.price:
           cheapest_flight.price = flight["price"]
           cheapest_flight.origin_airport = flight["flights"][0]["departure_airport"]["id"]
           cheapest_flight.destination_airport = flight["flights"][-1]["arrival_airport"]["id"]
           cheapest_flight.out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    return cheapest_flight
