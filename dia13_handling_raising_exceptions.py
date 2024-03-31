# Temperature conversion
def celsius_to_fahrenheit(celsius):
    try:
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    except TypeError:
        print("Error: The input value is not valid.")
        return None
try:
    temperature_celsius = float(input("Enter the temperature in Celsius: "))
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    if temperature_fahrenheit is not None:
        print("Temperature in Fahrenheit:", temperature_fahrenheit)
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# CPF validation
def validate_cpf(cpf):
    try:
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("Invalid CPF: it must contain exactly 11 numeric digits.")
        print("Valid CPF:", cpf)   # just a simplification
    except ValueError as e:
        print("Error:", e)
cpf = input("Enter the CPF (only numbers): ")
validate_cpf(cpf)

# Number division
def number_division():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        if denominator == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        result = numerator / denominator
        print("Division result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
number_division()

# TV series rating
def rate_tv_series(series_name, rating):
    try:
        rating = float(rating)
        if rating < 0 or rating > 10:
            raise ValueError("Invalid rating. Rating must be between 0 and 10.")
        print("You have rated the TV series '{}' with a rating of {}.".format(series_name, rating))
    except ValueError:
        print("Error: Invalid rating. Please enter a number between 0 and 10.")
series_name = input("Enter the name of the TV series: ")
series_rating = input("Enter your rating for the series (between 0 and 10): ")
rate_tv_series(series_name, series_rating)