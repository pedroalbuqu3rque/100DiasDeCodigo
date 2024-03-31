def add_numbers(n1, n2):
    print(n1 + n2)
add_numbers(6, 4)   # same function with different parameters
add_numbers(3, 5)

def add_numbers(*args):   # takes any number of arguments
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
add_numbers(1, 3, 5,  7, 9,)

def named(**kwargs):
    x = kwargs.get('surname4')   # takes any number of named arguments
    if x:
        print('Existing')
    else:
        print('Nonexistent')
named(surname1 = "Alves", surname2 = "Santos", surname3 = "Lima")

# Vowel counter
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter   # what is below will not be executed
word = input("Enter a word to count the vowels: ")
quantity_vowels = count_vowels(word)
print("The number of vowels in the word is:", quantity_vowels)

# Calculate the average of three numbers
def calculate_average(n1, n2, n3):
    return (n1 + n2 + n3) / 3
n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))
n3 = float(input('Enter the third number: '))
average = calculate_average(n1, n2, n3)
print('The average of the three numbers is:', average)
if average >= 6:
    print("The student passed.")
else:
    print("The student failed.")

# BMI calculator - body mass index
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def interpret_bmi(bmi):
    if bmi < 18.5:
        return 'Under Weight'
    elif 18.5 <= bmi < 25:
        return 'Normal Weight'
    elif 25 <= bmi < 30:
        return 'Overweight'
    else:
        return 'Obesity'
def main():
    name1 = input('Type your name: ')
    weight = float(input('Enter your weight in kg: '))
    height = float(input('Enter your height in meters: '))
    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)
    print(f'{name1}, your BMI is {bmi:.2f}, which indicates: {category}')
if __name__ == '__main__':
    main()
