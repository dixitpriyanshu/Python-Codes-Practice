import requests
from datetime import datetime

USERNAME = "" # Type a unique username
PIXELA_TOKEN = "" # type a unique key
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : PIXELA_TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
    
}

# response = requests.post(url = pixela_endpoint, json= user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Walking Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : PIXELA_TOKEN
}

# response = requests.post(url = graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year= 2022, month= 12, day= 31)

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "19.0"
}

# response = requests.post(url= pixel_creation_endpoint, json= pixel_data, headers= headers)
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "16.0"
}

# response = requests.put(url= update_endpoint, json= new_pixel_data, headers= headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url= delete_endpoint, headers= headers)
# print(response.text)