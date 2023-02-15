# with open("weather_data.csv") as file:
#     weather = file.readlines()
#     data = []
#     for x in weather:
#         weather_data = x.strip()
#         data.append(weather_data)
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     weather = csv.reader(file)
#     temperatures = []
#     for x in weather:
#         if x[1] != "temp":
#             temperatures.append(int(x[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# tem_list = data["temp"].tolist()
# print(tem_list)

# average = sum(tem_list) / len(tem_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_f = int(monday.temp) * 9/5 + 32
# print(monday_temp_f)

# data_dict = {
#     "names": ["a", "b", "c"],
#     "number": [1, 2, 3]
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_fur = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
# gray_count = len(gray_fur.index)
colors = ["Gray", "Cinnamon", "Black"]
counts = []
color_col = squirrel_data["Primary Fur Color"]
for x in colors:
    counts.append(len((squirrel_data[color_col == x]).index))

squirrels = {
    "Fur Color": colors,
    "Count": counts
}

squirrel_count = pandas.DataFrame(squirrels)
squirrel_count.to_csv("squirrel_count.csv")
