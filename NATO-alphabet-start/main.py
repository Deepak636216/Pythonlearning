import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
dictionary=pandas.read_csv("nato_phonetic_alphabet.csv")
nato={row.letter:row.code for (index,row)in dictionary.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter the word").upper()
phonetic_word=[nato[letter] for letter in word ]
print(phonetic_word)