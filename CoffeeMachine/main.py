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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order_ingredients):
    """Returns if there is enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there isn't enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""    
    print(f"Please insert coins.")
    total = int(input("How many dollars?: ")) * 1.00
    total += int(input("How many halves?: ")) * 0.50
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many pennies?: ")) * 0.5
    total += int(input("How many nickels?: ")) * 0.01
    return total


def successful_transaction(money_received, drink_cost):
    """Return True if payment accepted, or False when it is not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change.")
        # global scope, I have to declare it first
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink, ingredients):
    """Deduct ingredients from resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your coffee: {drink}")

######################MAIN???##############################################

profit = 0
is_on = True
# Prompt user
while is_on:
    choice = input("What do you like?(espresso/latte/cappuccino):")

    # Off button
    match choice:
        case "off":
            is_on = False
        case "report":
            # TODO: 1. Print report of all coffee machine resources
            print(f"Water: {resources['water']}ml")  # Imprime el tipo de 'water'
            print(f"Milk: {resources['milk']}g")  # Imprime el tipo de 'milk'
            print(f"Coffee: {resources['coffee']}g")  # Imprime el tipo de 'coffee'
            print(f"Money: {profit}$")
        case _:            
                drink = MENU[choice]
                if is_resource_enough(drink["ingredients"]):
                    payment = process_coins()
                    print(payment)
                    if successful_transaction(payment, drink["cost"]):
                        make_coffee(choice, drink["ingredients"])
                else:
                    print("Sorry, we do not have that drink.")
