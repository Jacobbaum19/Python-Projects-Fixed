import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Importing API keys from env
load_dotenv('env.txt')
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
Authorization = os.getenv("Authorization")

WEIGHT = 140
GENDER = "male"
AGE = 23
HEIGHT = 69

#--------------------------- Functions --------------------------- #
def lbs_to_kg(weight_lbs):
    return weight_lbs * 0.4535

def inches_to_cm(height_inches):
    return height_inches * 2.54

#--------------------------- Nutrientx API --------------------------- #

# Calling the functions and store the return values
weight_kg = lbs_to_kg(WEIGHT)
height_cm = inches_to_cm(HEIGHT)

user_input = input("What was your workout? ")

user_parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": AGE,
}
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Make the POST request to the Nutrionix API
nutrionix_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutrionix_api_url, headers=header, json=user_parameters)
response.raise_for_status()
response_json = response.json()

#--------------------------- Sheety API --------------------------- #

# Getting today's date to format into the sheet input
today_date = datetime.now()
time_now = today_date.strftime("%X")
today_date_formatted = today_date.strftime("%m/%d/%Y")

# Posting the request to the Google sheet
sheety_endpoint = "https://api.sheety.co/4f4395e6e61a94a2683039251c051d08/jacob'sTestWorkouts/workouts"

for exercise in response_json["exercises"]:
    sheet_inputs = {
    "workout": {
            "date": today_date_formatted,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": f"{round(exercise['duration_min'],0)} minutes",
            "calories": exercise["nf_calories"]
        }
    }
    header_sheety = {
        "Authorization": Authorization
    }
    sheet_response = requests.post(url=sheety_endpoint, headers=header_sheety, json=sheet_inputs)
    print(sheet_response.text)

#--------------------------- Testing... --------------------------- #
# Testing grabbing a row
# sheety_retrive_endpoint = "https://api.sheety.co/4f4395e6e61a94a2683039251c051d08/jacob'sTestWorkouts/workouts"
#
# retrieve_response = requests.get(url=sheety_retrive_endpoint)
# retrieve_response.raise_for_status()
# print(retrieve_response.text)
