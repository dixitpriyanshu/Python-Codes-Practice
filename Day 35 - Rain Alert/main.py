import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""           # Enter Your API Key

account_sid = "" # Enter your sid
auth_token = "" ## Enter your authentication token

weather_parameters = {
    "lat" : 12.971599,
    "lon" : 77.594566,
    "appid" : API_KEY
}
alt_weather_parameters = {
    "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : API_KEY
}

will_rain = False

response = requests.get(OWM_ENDPOINT, params= alt_weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☂",
    from_="+19704324339",
    to="Your Verified Number"
    )
    print(message.sid)