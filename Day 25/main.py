import pandas

data = pandas.read_csv("weather_data.csv")
# data_temp = data["temp"]
# print(data_temp.mean())
# print(data_temp.max())
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == max(data["temp"])])

monday = data[data.day == "Monday"]


def Fahrenheit(x): return (9/5)*x+32


print(Fahrenheit(int(monday.temp)))
