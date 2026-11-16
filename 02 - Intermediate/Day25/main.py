# import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# print(f"Average Temp: {data["temp"].mean()} degrees and the Max Temp was {data["temp"].max()} degrees.")

# print(data.condition)


monday = data[data.day == "Monday"]


# print(data[data["temp"] == data["temp"].max()])

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)

print(data)
data.to_csv("new_data.csv")