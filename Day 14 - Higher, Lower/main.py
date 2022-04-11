import random
from game_data import data


def selection(account):
    name = account['name']
    followers = account['follower_count']
    description = account['description']
    country = account['country']
    return f"{name} a {description} from {country}"


def comparison(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "A"
    else:
        return guess == "B"


flag = True

while flag:
    from art import logo

    print(logo)
    score = 0
    playing = False
    while not playing:
        choice_a = random.choice(data)
        choice_b = random.choice(data)
        if choice_a == choice_b:
            choice_b = random.choice(data)
        print("A)")
        print(selection(choice_a))
        follower_a = choice_a['follower_count']
        from art import vs

        print(vs)
        print("B)")
        print(selection(choice_b))
        follower_b = choice_b['follower_count']
        guess = input("Who has more followers, A or B? ")
        is_correct = comparison(guess, follower_a, follower_b)
        if is_correct:
            score += 1
            print(f"Correct! Current score: {score}")
        else:
            print(f"Incorrect. Current Score: {score}")
        again = input("Would you like to play again? Y or N: ")
        if again == "N":
            flag = False
        else:
            cont
