from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to have?{options}\n").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        #TODO 1.Print Report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #TODO 2. Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink):
            # TODO 3. Process coins.
            # TODO 4. Check transaction success
            if money_machine.make_payment(drink.cost):
                #TODO 5. Make Coffee
                coffee_maker.make_coffee(drink)
