import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiple(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide
}

def calculator():
    print(art.logo)

    reuse = True
    first_number = float(input("What's the first number? : "))

    while reuse:
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operator : ")
        second_number = float(input("What's the next number? : "))
        result = operations[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {result}")

        check = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()
        if check == "y":
            first_number = result
            reuse = True
        elif check == "n":
            reuse = False
            print("\n"*20)
            calculator()
        else:
            reuse = False
            print("Thank you for using the calculator")

calculator()


