import os

clear = lambda: os.system('cls')

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
# TODO 3. Print report.
# TODO 4. Check resources sufficient?
def materials(drink, ingredient_type):
    resource_check = resources[ingredient_type]
    ingredients_check = MENU[drink]['ingredients'][ingredient_type]
    if resource_check > ingredients_check:
        return True
    else:
        print(f"Not enough {ingredient_type}.")
        return False


def sufficient_resources(drink, ingredient_type):
    resources[ingredient_type] -= MENU[drink]['ingredients'][ingredient_type]


# TODO 5. Process coins.
def money_check():
    pennies = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))
    money = round(pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25, 2)
    print(f"Your current amount of money is ${money}.")
    return money


# TODO 6. Check transaction successful?
def money_calculator(user_money):
    available_coffee = MENU[drink]['cost']
    if user_money < available_coffee:
        print("Insufficient Funds.")
        return False
    else:
        return True


# TODO 7. Make Coffee.
making_coffee = True
while making_coffee:
    menu_stuff = True
    while menu_stuff:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "off":
            exit()
        elif drink == "report":
            print(f"Water: {resources['water']}m\n Milk: {resources['milk']}m\n Coffee: {resources['coffee']}g")
        else:
            menu_stuff = False
    milk_check = materials(drink,'milk')
    water_check = materials(drink, 'water')
    coffee_check = materials(drink, 'coffee')
    user_money = money_check()
    money_calculator(user_money)
    print(f"Your {drink} is now dispersed. Enjoy!")
    change = round(user_money - MENU[drink]['cost'], 2)
    print(f"Your change is ${change}.")
    sufficient_resources(drink, 'milk')
    sufficient_resources(drink, 'water')
    sufficient_resources(drink, 'coffee')
    again = input("Would you like another? Y or N? ")
    if again == "Y":
        clear()
        continue
    else:
        making_coffee = False
