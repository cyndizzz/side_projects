import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_agg = data['Primary Fur Color'].value_counts()
color_agg.to_csv('squirrel_count.csv')

