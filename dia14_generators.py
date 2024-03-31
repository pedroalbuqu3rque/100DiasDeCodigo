def even_number_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i   # produces a value each time the function is called
gen = even_number_generator(10)
for num in gen:
    print(num)

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
gen = fibonacci_generator(10)
for num in gen:
    print(num)

def prime_generator(n):
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
gen = prime_generator(20)
for num in gen:
    print(num)

