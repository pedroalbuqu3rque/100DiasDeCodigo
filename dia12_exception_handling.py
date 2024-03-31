# math_operations
'''
def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

import math_operations

print("Sum:", math_operations.sum(5, 3))
print("Subtraction:", math_operations.subtraction(10, 4))
print("Multiplication:", math_operations.multiplication(3, 7))
print("Division:", math_operations.division(10, 2))
print("Division by zero:", math_operations.division(8, 0))
'''

def divide_numbers():
    try:   # allows the program to continue executing even if an exception occurs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print("The result of the division is:", result)

    except ValueError:
        print("Error: Invalid input. Please enter only numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    divide_numbers()