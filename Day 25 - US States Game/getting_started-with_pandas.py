import pandas
def convert_temp(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

data  = pandas.read_csv("Day 25 - US States Game/weather_data.csv")
print(data)
print("\n")
print(data["temp"])
print("\n")

# temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# print(round(average))

print(data["temp"].mean())

##get max Temperature

print(data["temp"].max())

##########    Getting data in Columns

print(data["condition"])
print(data.condition)

###### Get data in Row

print(data[data.day == "Monday"])

#### Get Row with max temperature

print(data[data.temp == data.temp.max()])

## getting particular data from particular row

monday = data[data.day == "Monday"]

print(monday.condition)
temp_c = int(monday.temp)
temp_f = convert_temp(temp_c)
print(temp_f)


##### Create a DataFrame from Scratch

data_dict = {
    "students": ["Amy", "Sheldon", "Raj"],
    "scores": [76, 55, 64]
}

new_data = pandas.DataFrame(data_dict)

print(new_data)
new_data.to_csv("Day 25 - US States Game/new_data.csv")