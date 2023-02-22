import pandas
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

run_loop = True
while run_loop:
    user_word = input("What's is the word? ").upper()
    try:
        user_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters of the alphabet are allowed.")
    else:
        run_loop = False
        print(user_list)
