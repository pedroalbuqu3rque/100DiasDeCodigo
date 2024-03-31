class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Lucas", 31)
person2 = Person("Jonas", 23)

print(person1.name)
print(person2.name)

class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2018)

print(car1.make, car1.model, car1.year)
print(car2.make, car2.model, car2.year) 