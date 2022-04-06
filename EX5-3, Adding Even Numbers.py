#Write your code below this row 👇
totalsum = 0
for number in range(1, 101):
    if number % 2 == 0:
        totalsum += number
print(totalsum)