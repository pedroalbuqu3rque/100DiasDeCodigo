def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1
prime_gen = prime_generator()
print("The first 10 prime numbers:")
for _ in range(10):
    print(next(prime_gen))

# Write a function that takes a list of numbers and returns a new list with each element multiplied by 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))   # "map" applies a function to each item in a sequence
print(doubled_numbers)

# Write a function that takes a list of numbers and returns a new list with only the even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))   # "filter" creates an iterator filtering the elements of a sequence
print(even_numbers)