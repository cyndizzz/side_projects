import pandas as pd

#TODO 1. Create a dict in this format {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv')
dict = { row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ")
list_input = list(user_input.upper())
output_list = [ value  for (key,value) in dict.items() if key in list_input ]
print(output_list)