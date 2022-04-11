import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def game():
    flag = True
    while flag:
        from art import logo
        print(logo)
        print("Welcome to the Number Guessing Game!")
        ran_num = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100")
        choice = input("Please enter a difficulty: Easy or Hard: ")
        if choice == "Easy":
            num_guesses = 10
        elif choice == "Hard":
            num_guesses = 5
        while num_guesses != 0:
            print(f"Number of Guesses is {num_guesses}")
            guess = int(input("Please guess the number: "))
            if guess > ran_num:
                print("Too High.")
                num_guesses -= 1
            elif guess < ran_num:
                print("Too Low.")
                num_guesses -= 1
            elif guess == ran_num:
                print("Correct. Great job, you sexy bastard!")
                num_guesses = 0
        again = input("Would you like to play again? Y or N: ")
        if again == "N":
            flag = False
        else:
            cls()



game()
