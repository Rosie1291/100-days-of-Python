# Menu
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

# ask user for input (while loop -> ends when "off")
user_drink = input("What would you like? (espresso/latte/cappuccino): ")
print(MENU[user_drink]["cost"])

# var
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
profit = 0


def check_sufficient_resources(order_ingredients):
    # return True if all input values are > 0, else return False
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def total_coins():  # function to calculate input coins
    coins = {
        "quarters": 0.25,
        "dimes": 0.1,
        "nickels": 0.05,
        "pennies": 0.01
    }
    print("Please insert coins: \n")
    total = sum(int(input(f"How many {coins}? ")) * value for coin, value in coins.items())
    return total


def transaction_success(user_payment, cost):  # compare money received vs cost
    if user_payment >= cost:
        change = round(user_payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print(f"Sorry the money is insufficient. Money refunded.")
        return False

order_ingredients = MENU[user_drink]["ingredients"]
# check user's input -> check resources (loop all 3):
while check_sufficient_resources(order_ingredients):
    print("Please insert coins.")
    quarters = input("how many quarters? ")
    dimes = input("how many dimes? ")
    nickels = input("how many nickels? ")
    pennies = input("how many pennies? ")

# if enough: -> ask coins input -> calculate coins -> compare against price
# -> if not: return money,
# -> if enough: change in resources and money report
# -> if more: print returned coins and change in resources and money report
# -> print: Enjoy drink!
# if not enough: nothing deducted, money refund
# print report (water, milk, coffee, money)
