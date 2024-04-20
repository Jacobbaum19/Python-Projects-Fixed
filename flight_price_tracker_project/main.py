from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
sheet_data = dm.get_data()
print(sheet_data)
# Checks to see if the iataCode row is empty
if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        """Grabs the city_name and iata_code and sends them to dm. Sheet is then autopopulated with Iatacodes.
        Price is feteched with the new Iatacodes and new_price and new_link is created from them. 
        Checks to see if new_price is not empty and the new price is lower than the existing price on the
        sheet."""
        
        city_name = row["city"]
        iata_code = dm.get_iata_code(city_name)
        row["iataCode"] = iata_code
        dm.update_sheet(row, iata_code)
        print(f"Fetching price for {city_name} with IATA code {iata_code}")
        new_price, new_link = flight_search.get_price_for_flight(city_name, iata_code)
        
        if new_price and new_price < row["lowestPrice"]:
            dm.update_sheet_price_url(row, new_price, new_link)
            print(f"Lower price found for {city_name}: €{new_price}")
    print("Thank you for using Jacob's flight price checker! Take care!")
