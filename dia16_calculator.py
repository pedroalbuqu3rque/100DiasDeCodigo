def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: division by zero"

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def calculate(operator, x, y):
    if operator in operations:
        return operations[operator](x, y)
    else:
        return "Invalid operation"

def calculator():
    print("Available operations: +, -, *, /")
    operator = input("Enter the desired operator: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculate(operator, num1, num2)
    print("Result:", result)

calculator()