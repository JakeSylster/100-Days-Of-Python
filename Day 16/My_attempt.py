from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#drink = MenuItem("")
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#TODO 1.Print Report
coffee_maker.report()
money_machine.report()

drink = input(f"What would you like to have?{menu.get_items()}\n")
drink_choice = menu.find_drink(drink)

#TODO 2. Check resources sufficient?
coffee_maker.is_resource_sufficient(drink_choice)

#TODO 3. Process coins.
#money_machine.process_coins()

#TODO 4. Check transaction success
money_machine.make_payment(drink_choice.cost)

#TODO 5. Make Coffee
coffee_maker.make_coffee(drink_choice)
