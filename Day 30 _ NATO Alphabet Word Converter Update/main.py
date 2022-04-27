import pandas

# Use Pandas to get data
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# Take user input and convert to data from pandas
def NATO_Generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry. Only letters are allowed.")
        NATO_Generate()
    else:
        print(output_list)


NATO_Generate()
