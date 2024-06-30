from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True


# TODO 1: Print report
# calling my report object in coffee maker class
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

# # TODO main stuff
while machine_on:
    menu = Menu()
    drink_options = menu.get_items()
    user_input = input(f"What would you like? {drink_options}: ")
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        # TODO 1.5 get drink from menu
        # check if resources are sufficient to make drink
        # first get drink from the menu class
        drink = menu.find_drink(user_input)
        # print(drink)
        # checking for sufficient resource
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)

