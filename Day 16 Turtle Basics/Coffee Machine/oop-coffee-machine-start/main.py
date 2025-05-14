from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:

    print(f"What would you like: {menu.get_items()}")
    choice = input()

    if choice=="off":
        break
    elif choice=="report":
        coffee_machine.report()
        money_machine.report()
    else:
        # drink will return an object of MenuItem Class
        drink = menu.find_drink(choice)
        if drink and coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)