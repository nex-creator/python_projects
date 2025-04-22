# with open("weather_data.csv", mode ='r') as file:
#     data = file.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pd.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

# data_dict= data.to_dict()
# print(data_dict)
# print(data["temp"].mean())
# print(data["temp"].max())
# # get data in column
# print(data["condition"])
# print(data.condition)

# get data in rows
#print(data[data.day == "Monday"])
# extract the row which has highest weather in the week

#
# monday = (data[data.day== "Monday"])
# far_scale = (monday.temp * 9/5)+32
# print(far_scale)

# create a datafram from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
# data_1 = pd.DataFrame(data_dict)
# print(data_1)
# data_1.to_csv("new_data.csv")
# import pandas as pd
# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
# }
# data_1 = pd.DataFrame(data_dict)
# data_1.to_csv("squirrels_data.csv")

import pandas

student_dict = {
    "student":["Angela","James","Lily"],
    "score": [56,76,98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for(index,row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)





























