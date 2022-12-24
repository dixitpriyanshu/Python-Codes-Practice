import pandas

data  = pandas.read_csv("Day 25 - US States Game/squirrel_table.csv")
fur_data = data["Primary Fur Color"].to_list()

gray_count = fur_data.count("Gray")
cinnamon_count = fur_data.count("Cinnamon")
black_count = fur_data.count("Black")

count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

table_data = pandas.DataFrame(count_dict)

table_data.to_csv("Day 25 - US States Game/squirrel_count.csv")

######################## ALternate Code ##################################

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")