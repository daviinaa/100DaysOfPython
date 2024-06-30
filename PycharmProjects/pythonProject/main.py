MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


machine_off = False


def sufficient_resources(drink_choice):
    for items in drink_choice:
        if drink_choice[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


resources["money"] = int("0")


def process_coin():
    print("Please insert coins")
    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")
    total = ((int(quarters) * 0.25) + (int(dimes) * 0.10) + (int(nickles) * 0.05) + (int(pennies) * 0.01))
    return total


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change ${change}")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_choice, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here's your {drink_choice} enjoy!")


while not machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine_off = True
    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[user_choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment, MENU[user_choice]["cost"]):
                make_coffee(user_choice, drink["ingredients"])
