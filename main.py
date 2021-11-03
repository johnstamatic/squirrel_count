# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures[1])
#
# import pandas
#
# data =  pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# # temp_list = data["temp"].to_list()
#
# # # average = sum(temp_list) / len(temp_list)
# # # print(average)
# # print(data["temp"].max())
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# # monday = data[data.temp == "12"]
# # print(monday)
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)
#
# print(monday_temp)

import pandas

# using valuecounts method
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data["Primary Fur Color"].value_counts()
new_file = pandas.DataFrame(gray)
new_file.to_csv("squirrel_count.csv")

#using class solution
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count2.csv")





