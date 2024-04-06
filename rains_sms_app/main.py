import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Loading in ENV variables...
load_dotenv('env.txt')

OMM_Endpoint = os.getenv('OMM_Endpoint')
api_key = os.getenv('api_key')
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')


parameters = {
    "lat": 43.880318,
    "lon": -103.453873,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OMM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()


# Create a list of IDs for weather
weather_data_ids = [weather_data["list"][i]["weather"][0]["id"] for i in range(4)]

# Create a dictionary to create a key for each value
weather_data_dict = {f"{i*3}_hrs:": weather_data["list"][i]["weather"][0]["id"] for i in range(4)}

print(weather_data_dict)

## Weather Codes
# 200-232: Thunderstorm
# 300-321: Drizzle
# 500-531: Rain
# 600-622: Snow
# 701-781: Atmosphere (mist, fog, etc.)
# 800: Clear
# 801-804: Clouds


umbrella_needed = False
for weather_id in weather_data_dict.values():
    if 200 <= weather_id <= 531:
        umbrella_needed = True
        break  # Stops checking once it finds a rain value.

if umbrella_needed:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella! 🌧️",
        from_='+18446182037',
        to='+2849349831',  # Random number, Twilio can't send messages to
        # toll-free numbers without verifying you're a company...
    )
    print(message.status)
