import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(f"Gray: {gray}\nRed: {red}\nBlack: {black}")

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")