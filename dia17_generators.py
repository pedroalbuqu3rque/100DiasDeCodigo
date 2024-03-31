numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)   # filter even numbers
print(list(even_numbers))

temperatures_celsius = [0, 10, 20, 30, 40]
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
temperatures_fahrenheit = map(celsius_to_fahrenheit, temperatures_celsius)   # apply the function to each element
print(list(temperatures_fahrenheit))

strings = ["Richard", "Jared", "Erlich", "Gilfoyle", "Monica"]
lengths = map(len, strings)
print(list(lengths))