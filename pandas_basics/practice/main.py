# # import csv
# # with open("weather_data.csv")as data_file:
# #     data=csv.reader(data_file)
# #     temperatures=[]
# #     for row in data:
# #         temperatures.append(row[1])
# #     print(temperatures)    
# import pandas 
# data=pandas.read_csv("weather_data.csv")
# # temp_list=data["temp"].to_list()
# # print(data["temp"].max())
# print(data[data["day"]=="Monday"])
# print(data[data["temp"]==data["temp"].max()])
import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray=len(data[data["Primary Fur Color"]=="Gray"])
red=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])

print(gray,red,black)
data_dict={
    "PrimaryfurColor":["Gray","red","black"],
    "count":[gray,red,black]
}
pandas.DataFrame(data_dict)