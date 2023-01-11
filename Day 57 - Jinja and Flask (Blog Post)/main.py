import requests
name = "priyanshu"
age = requests.get(f"https://api.agify.io/?name={name}").json()['age']
gender = requests.get(f"https://api.genderize.io/?name={name}").json()['gender']
