import requests
import os
from dotenv import load_dotenv

# Loading in the Environment variables
load_dotenv("env.txt")

TEQUILA_ENDPOINT = os.getenv("TEQUILA_ENDPOINT")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
sheet_put_endpoint = os.getenv("sheet_put_endpoint")
sheety_api_endpoint = os.getenv("sheety_api_endpoint")


class DataManager:
    def get_data(self):
        try:
            """Gets the initial table that should be made otherwise a FileNotFound Error will show."""
            self.request = requests.get(url=sheety_api_endpoint)
            self.request_json = self.request.json()
            sheet_data = self.request_json["prices"]
            print(sheet_data)
            return sheet_data
        except FileNotFoundError:
            print("File could not be found!")

    def get_iata_code(self, city_name):
        parameters = {
            "location_types": "city",
            "term": city_name,
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=parameters, headers=headers)
        # print(response.text)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def update_sheet(self, city, code):
        new_data = {
            "price": {
                "iataCode": code,
            }
        }
        response = requests.put(url=f"{sheet_put_endpoint}/{city['id']}", json=new_data)
        # print(response.text)

    def update_sheet_price_url(self, city, new_price, url):
        new_data = {
            "price": {
                "url": url,
                "Lowest Price": new_price
            }
        }
        response = requests.put(url=f"{sheet_put_endpoint}/{city['id']}", json=new_data)
        # print(response.text)
