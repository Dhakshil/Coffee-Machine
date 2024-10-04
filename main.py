MENU = {
    "espresso": {
        "ingredients": {
            "water": 10,
            "coffee": 28,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 20,
            "milk": 50,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 60,
            "coffee": 30,
        },
        "cost": 300,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(components):
    for item in components:
        if components[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins or money.")
    while True:
        try:
            total = int(input("Enter the amount you inserted: "))
            return total
        except ValueError:
            print("Invalid input. Please enter a valid amount.")



def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is Rs.{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded Rs.{money_received}.")
        return False


def make_coffee(drink_name, components):
    for item in components:
        resources[item] -= components[item]
    print(f"Here is your {drink_name} ☕️. Enjoy your Drink!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print(f"Please check your typo. Thanks!")