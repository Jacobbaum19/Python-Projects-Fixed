import requests
from datetime import datetime
import time
import smtplib

""" This project's goal was to send an email when NASA's ISS is above your location (Latitude and Longitude). 
Fake emails were used but can be replaced with your own, as well as your coordinates."""

# Email information
my_email = "patricag912@gmail.com"
password = "ocovlxxjggeuanyh"

# Getting the current time
time_now = datetime.now()
time_now_hour = time_now.hour

# Constants
MY_LAT = 39.585258
MY_LONG = -105.084419
MARGIN_OF_ERROR = 5


# ----------------------- API ---------------------- #

# Start of the API requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# Converting the data to json and getting the lat and long coordinates from it
data_iss = response.json()
iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])
iss_position = (iss_latitude, iss_longitude)

# Parameter for API
parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# ----------------------- Sunset/Sunrise times for location ---------------------- #
# Sunset and Sunrise times

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data_sunrise_sunset = response.json()
sunrise = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])

print(f"Your sunset time is: {sunset} PM (UTC)")

# ----------------------- Functions ---------------------- #


def iss_is_above():
    # Check if the ISS latitude and longitude are within the specified margin of error
    is_within_margin = (MY_LAT - MARGIN_OF_ERROR <= iss_latitude <= MY_LAT + MARGIN_OF_ERROR) \
                       and (MY_LONG - MARGIN_OF_ERROR <= iss_longitude <= MY_LONG + MARGIN_OF_ERROR)

    # Check if the current time is after 12 PM (noon)
    is_after_noon = time_now_hour >= 12

    # Check if the ISS is above the location and it's after noon
    if is_within_margin and is_after_noon:
        send_email_notification()
        return True
    else:
        return False


def send_email_notification():
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: The ISS is above your location! \n\n Look up, the ISS should be visible soon.")

# ----------------------- Running the code every minute ---------------------- #


# Gets code to run every 60 seconds
while True:
    result = iss_is_above()
    print(result)
    time.sleep(60)
