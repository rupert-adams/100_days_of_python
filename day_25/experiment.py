import pandas as pd

data = pd.read_csv('data/weather_data.csv')
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

temp_total = 0

for item in temp_list:
    temp_total+=item

adverage_temp = temp_total/len(temp_list)
adverage_temp_2 = data["temp"].mean()
print(adverage_temp)
print(adverage_temp_2)


print(data[data["temp"] == data["temp"].max()])

monday = data[data["day"] == "Monday"]

monday_temp = int(monday["temp"])
print(monday_temp)

data_dict = {
    "students": ["Mike", "Paul"],
    "scores": [40, 80]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv('data/student_data.csv')
