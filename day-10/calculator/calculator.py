import art

print(art.logo + "\n")

# Calculator
# Add


def add(a, b):
    return a + b

# Subtract


def subtract(a, b):
    return a - b

# Multiply


def multiply(a, b):
    return a * b

# Divide


def divide(a, b):
    return a / b


# Create a dict of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
}

def calculator():
    num1 = float(input("Enter a first number: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue:

        operation_key = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        operation = operations[operation_key]
        answer = operation(num1, num2)

        print(f"{num1} {operation_key} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()