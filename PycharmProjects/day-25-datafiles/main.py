# with open("weather_data - Sheet1.csv") as data:
#     data.read()

# with open("weather_data - Sheet1.csv") as list:
#     data = list.readlines()
# print(data)
# import csv

# with open("weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data_file = pandas.read_csv("weather_data - Sheet1.csv")
# converts the data csv to dictionary
# print(data_file.to_dict()["day"])
# print(data_file["temp"])

# convert series to list
# temp_list = data_file["temp"].to_list()
# avg_list = sum(temp_list) / len(temp_list)
# print(len(temp_list))
# print(temp_list)
# print(avg_list)
# mean value
# mean = data_file["temp"].mean()
# print(mean)

# max value
# maximum_val = data_file["temp"].max()
# print(maximum_val)

# how to get the row in the data csv file, filtering it by the max temperature
# print(data_file[data_file.temp == data_file.temp.max()])

# get a single data value
# Monday = data_file[data_file.day == "Monday"]
# monday_temp = Monday.temp
# mon_temp_F = monday_temp[0] * 9/5 + 32
# print(mon_temp_F)

# SQUIRREL count challenge
# import pandas as pd
#
# sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240622.csv")
# grey_num = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
# red_num = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
# black_num = len(sq_data[sq_data["Primary Fur Color"] == "Black"])
# print(grey_num)
# print(red_num)
# print(black_num)
#
# sq_dict = {
#     "fur color": ["grey", "cinnamon", "black"],
#     "count": [grey_num, red_num, black_num]
# }
#
# data_new = pd.DataFrame(sq_dict)
# data_new.to_csv("challengedone.csv")
# print(data_new)
# print(sq_data["Primary Fur Color"].to_list())
