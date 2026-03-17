import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    should_cumulate = True
    num1 = None

    while num1 is None:
        try:
            num1 = float(input("What's the first number?: "))
        except ValueError:
            print("Invalid input, please try again")

    while should_cumulate:
        for symbol in operations:
            print(symbol)

        operator = None
        num2 = None

        while operator is None:
            try:
                operator = input("Pick an operator: ")
            except ValueError:
                print("Invalid input, please try again")

        while num2 is None:
            try:
                num2 = float(input("What's the next number?: "))
            except ValueError:
                print("Invalid input, please try again")

        num = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {num}")

        choice = input(f"Type 'y to continue calculating with {num}, or type 'n' to start new calculation: ")
        if choice.lower() == "n":
            should_cumulate = False
            print('\n'*20)
            calculator()
        elif choice.lower() == 'y':
            num1 = num
        else:
            exit

calculator()