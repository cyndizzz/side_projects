import pandas as pd

#TODO 1. Create a dict in this format {"A": "Alfa", "B": "Bravo"}

df = pd.read_csv('nato_phonetic_alphabet.csv')
dict = { row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
output_list = [ dict[letter] for letter in user_input ]
print(output_list)