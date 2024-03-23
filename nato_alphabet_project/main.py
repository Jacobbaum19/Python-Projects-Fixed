import pandas
# Create a dataframe from CSV
nato_alpahabet_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alpahabet_df = pandas.DataFrame(nato_alpahabet_csv)
nato_words = nato_alpahabet_df.code


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (_, row) in nato_alpahabet_df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_keeps_going = True
while user_keeps_going:
    user_input = input("Choose a word to be converted spelled out with the NATO alphabet? ").lower()
    if user_input != "stop":
        user_input_nato = [nato_dict[letter.upper()] for letter in user_input]
        print(user_input_nato)
    if user_input == "stop":
        user_keeps_going = False
