import random
import os
clear = lambda: os.system('cls')

def deal():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_list)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else:
        return sum(cards)


def compare_hands(user_score, comp_score):
    if user_score > 21 and comp_score > 21:
        return "You went over. You lose 😤"
    if user_score == comp_score:
        return "Draw 🙃"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    from art import logo
    print(logo)

    user_hand = []
    comp_hand = []
    is_game_over = False
    print("Welcome to Blackjack!")

    for _ in range(2):
        user_hand.append(deal())
        comp_hand.append(deal())

    while not is_game_over:
        user_score = calculate_score(user_hand)
        comp_score = calculate_score(comp_hand)
        print(f"Your current hand is {user_hand} with a score of {user_score}")
        print(f"Dealer's  is {comp_hand[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            player_choice = input("Would you like another card? Y or N? ")
            if player_choice == "Y":
                user_hand.append(deal())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_hand.append(deal())
        comp_score = calculate_score(comp_hand)

    print(f"Your final hand is {user_hand} with a score of {user_score}.")
    print(f"Dealer's final hand is {comp_hand} with a score of  {comp_score}")
    print(compare_hands(user_score, comp_score))


if input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ") == "Y":
    clear()
    play_game()
