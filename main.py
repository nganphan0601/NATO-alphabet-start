import pandas as pd

# get the user's name
name = input("What is your name? ")
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# read the csv file as a dataframe 
nato_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_dataframe)

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in nato_dataframe.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
result = [nato_dict[letter.upper()] for letter in name]

print(result)