x = {1, 2, 3, 4, 5}
y = {5, 7, 8, 9, 10}
t = x.union(y)   # "intersection", "difference", "symmetric_difference"
print(t)

def my_function():   # defines what will be executed
    sum = 0
    for i in range(0, 101):
        sum = sum + i
    print(sum)
my_function()   # execute

def reverse_string(text):
    return text[::-1]
text = "After all this time?"
print("Inverted text:", reverse_string(text))

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = 7
print(num, "is:", check_even_odd(num))