import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv('env.txt')
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
Graph_ID = "graph1"

# Step 1: Creating the initial graph
user_parameters = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


pixela_endpoint = "https://pixe.la/v1/users"

response = requests.post(url=pixela_endpoint, json=user_parameters)

# Step 2: Setting up the graph with the color and title
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": Graph_ID,
    "name": "Python Coding Days",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response_2 = requests.post(url=graph_endpoint,json=graph_config, headers=headers)

# Step 3: Posting a pixel to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_ID}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

user_parameters_posting_pixel = {
    "date": today_formatted,
    "quantity": "4",
}

response_3 = requests.post(url=pixel_creation_endpoint,json=user_parameters_posting_pixel, headers=headers)

# Step 4: Update a pixel in the graph
update_pixel = {
    "date": today_formatted,
    "quantity": "2",
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_ID}/{today_formatted}"
response_4 = requests.put(url=pixel_creation_endpoint,json=update_pixel, headers=headers)

# Step 5: Delete a pixel

# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{Graph_ID}/{today_formatted}"
# response_5 = requests.delete(url=pixel_creation_endpoint, headers=headers)
