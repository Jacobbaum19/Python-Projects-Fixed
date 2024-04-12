import os
import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT_SEARCH = os.getenv("TEQUILA_ENDPOINT_SEARCH")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def get_price_for_flight(self, city_name, code):
        # Calculate date 60 days from today
        date_from = datetime.now()
        date_to = date_from + timedelta(days=60)

        # Format dates for API
        date_from_formatted = date_from.strftime("%d/%m/%Y")
        date_to_formatted = date_to.strftime("%d/%m/%Y")

        # Set up the parameters for the flight search
        params = {
            "fly_from": "DEN",
            "fly_to": code,
            "date_from": date_from_formatted,
            "date_to": date_to_formatted,
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }

        # Make the API request. Checks after new_price and link in case the data can't be found.
        response = requests.get(url=TEQUILA_ENDPOINT_SEARCH, params=params, headers=headers)
        if response.status_code == 200:
            flight_data = response.json()
            new_price = flight_data['data'][0].get("price", "Price not available")
            link = flight_data["data"][0].get("deep_link", "URL not available")
            return new_price, link
        else:
            print(f"Error fetching flights for {city_name}: {response.status_code}")
            return None, None


# Testing how it works

# fs = FlightSearch()
# fs.get_price_for_flight("Paris", "PAR")
