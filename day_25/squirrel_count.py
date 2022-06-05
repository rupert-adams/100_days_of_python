import pandas as pd

data = pd.read_csv('data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

colour_list = data['Primary Fur Color'].unique()[1::1]
colour_dict = {}

for colour in colour_list:
    colour_dict[colour] = data['Primary Fur Color'][data['Primary Fur Color'] == colour].count()

colour_df = pd.DataFrame(list(colour_dict.items()), columns=["fur_colour", "num_of_squirrels"])

colour_df.to_csv('output_data/squirrel_count.csv')

