import requests
from datetime import datetime

APP_ID = "" # Your APP ID
API_KEY = "" # Your API Key
GENDER = "male"
WEIGHT = 54
HEIGHT = 172
AGE = 22

nutritionnix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "" # Your Sheety Endpoint for post request
nutritionnix_header = {
    "x-app-id" : APP_ID,
    "x-app-key" :API_KEY
}

exercise_input = input("Tell me which exercise you did: ")

nutritionnix_parameters = {
    "query" : exercise_input,
    "gender" : GENDER,
    "weight_kg" : WEIGHT,
    "height_cm" : HEIGHT,
    "age" :  AGE
}

response = requests.post(
    url = nutritionnix_exercise_endpoint,
    json = nutritionnix_parameters,
    headers = nutritionnix_header
)

result = response.json()["exercises"]
print(result)
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

for exercise in result:
    sheety_parameters = {
        "workout" : {
        "date" : date,
        "time" : time,
        "exercise" :exercise["name"].title(),
        "duration" : exercise["duration_min"],
        "calories" : exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url= sheety_endpoint, json= sheety_parameters)
    print(sheet_response.text)
