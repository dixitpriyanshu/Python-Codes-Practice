import requests

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "52b129a4bc23d481dc754462e14323d2"

weather_parameters = {
    "lat" : 12.971599,
    "lon" : 77.594566,
    "appid" : API_KEY
}

response = requests.get(OWM_ENDPOINT, params= weather_parameters)
print(response.status_code) 