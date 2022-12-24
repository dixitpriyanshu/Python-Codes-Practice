weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def to_f(c):
    f = (c * 9/5) + 32
    return f

weather_f = {day : to_f(temp_c) for (day, temp_c) in weather_c.items()}


print(weather_f)


