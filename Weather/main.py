## Handle as txt
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#
# print(data)

## Handle as csv
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#
#     print(temperatures)

## Alternative: Pandas
import pandas as pd

data = pd.read_csv('weather_data.csv')          # data is a dataframe
print(data['temp'])                             # data['temp'] is a series.

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)
print(len(temp_list))

# Estimate the avg temp.
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)

print(data['temp'].mean())
print(data['temp'].max())

# Get Data in Columns
print(data['temp'])             # Treating data as a dictionary, pulling each column by calling the key.
print(data.temp)                # Treating it as an object, holding the data in that column.

# Get Data in Rows
print(data[data.day == 'Monday'])

# Challenge: Which day has the highest temperature.
print(data[data.temp == data.temp.max()]['day'])


monday = data[data.day == 'Monday']
monday_temp = monday.temp[0]
print(monday_temp * 9/5 + 32)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_new = pd.DataFrame(data_dict)
print(data_new)
data_new.to_csv('new_data.csv')


