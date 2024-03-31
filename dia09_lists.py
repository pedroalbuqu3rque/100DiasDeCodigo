numbers = [1, -2, 3, -4, 5]
positives = [num for num in numbers if num > 0]
print(positives)   # "num" is a temporary variable used to reference each item in the 'numbers' list during the creation of the 'positives' list

person = {'name': 'João', 'age': 7, 'number': '4002-8922', 'favorite color': 'Pink' }
person['name'] = 'João Pedro'
print(person['name'])

people = {'names': [], 'age': 23}
people['names'].append('Carlos Alves')   # add to list
people['names'].append('João Araújo')
print(people['names'][0])

people = [{'name': 'Lucas', 'age': 26, 'height': 173}, 
          {'name': 'André', 'age': 21, 'height': 170}, 
          {'name': 'Davi', 'age': 19, 'height': 168}]
for person in people:
    print(person['name'])

# Write a program where the user can register 'n' people, storing their name, age, and height
people = []
while True:
    decision = int(input('To register a person, type 1, and to exit, type 2: '))
    if decision == 2:
        break
    person = {'name': input('Please enter the name: '), 
              'age': input('Please enter the age: '), 
              'height': input('Please enter the height: ')}
    people.append(person)
print(people)

person = {'name': 'Cillian Murphy', 'age': 47, 'height': 170}
person.update({'wife': 'Yvonne McGuinness', 'birthday': 'May 25, 1976'})  # It's being added to the list 
print(person)

animal = {'name': 'Jack', 'breed': 'Labrador Retriever', 'size': 'Medium', 'weight': 63}
print( animal.values())
print( animal.keys())

# Combining lists into dictionary with aggregated values
names = {'Gabriel', 'Júnior', 'Luana', 'Geovana'}
ages = {34, 14, 26, 19}
people = {name: age for name, age in zip(names, ages)}   # Combines elements from two or more sequences into tuples
print(people) 