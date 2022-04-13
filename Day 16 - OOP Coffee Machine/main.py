from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_methods = CoffeeMaker()
money = MoneyMachine()

making_coffee = True
while making_coffee:
    flag = True

    while flag:
        order_name = input("What would you like? (espresso/latte/cappuccino/): ")
        if order_name == "report":
            coffee_methods.report()
            money.report()
        elif order_name == "off":
            exit()
        else:
            flag = False

    drink = coffee_menu.find_drink(order_name)
    resource_check = coffee_methods.is_resource_sufficient(drink)

    if not resource_check:
        print("Insufficient Resources :(")
        exit()

    money.make_payment(drink.cost)
    coffee_methods.make_coffee(drink)

    again = input("Would you like another? Y or N: ")
    if again == "N":
        making_coffee = False

