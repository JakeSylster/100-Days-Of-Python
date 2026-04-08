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

profit = 0
coffee_machine = {
        "water": 300,
        "milk" : 200,
        "coffee": 100,
}

# TODO 4. Check resource availability
def check_resource_availability(order_ingredients):
    """Returns True when order can be made and False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > coffee_machine[item]:
            print(f"Sorry! there is not enough of {item} to fulfill your order.")
            return False
    return True

#TODO 5. Process coins
def process_coins():
    """Returns the total money inserted into the system"""
    print("Please insert coins for the desired drink:")
    quarters = int(input("How many quarters:"))
    dimes =  int(input("How many dimes:"))
    nickel =  int(input("How many nickels:"))
    pennies =  int(input("How many pennies:"))
    total_money = quarters*0.25 + dimes*0.10 + nickel*0.05 + pennies*0.01
    return total_money

# TODO 6. Check transaction successful
def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        if money_received > drink_cost:
            print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry! that's not enough money. Money refunded.")
        return False

# TODO 7. Making Coffee
def make_coffee(drink_name, order_ingredients):
    """Make the desired drink.Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        coffee_machine[item] -= order_ingredients[item]
    print(f"Here is your order {drink_name} ☕️")


# TODO 1. Ask user for choice of drink
is_on = True
while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino) ")

    # TODO 2. Turn machine off
    if choice == "off":
        print("The machine is turned off")
        is_on = False

    # TODO 3. Print report
    elif choice == "report":
        for key in coffee_machine:
            print(f"{key} : {coffee_machine[key]}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resource_availability(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
