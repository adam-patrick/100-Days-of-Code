numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Adam"

letters_list = [letter for letter in name]
print(letters_list)

double_list = [num * 2 for num in range(1, 5)]
print(double_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elenor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)
