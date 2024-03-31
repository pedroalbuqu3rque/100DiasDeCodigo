# create a class called vehicle with attributes brand and model. then, create an object of this class and print its characteristics
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_vehicle = Vehicle("Ford", "Fiesta")

print("Brand:", my_vehicle.brand)
print("Model:", my_vehicle.model)

# create a person class with name and age attributes. then, create objects of this class and modify their attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Pedro", 19)
person2 = Person("Lucas", 25)

person1.name = "Albus"
person2.age = 28

print("Person 1 - Name:", person1.name, "Age:", person1.age)
print("Person 2 - Name:", person2.name, "Age:", person2.age)

# create a math class with a class method called sum that receives two numbers as arguments and returns the sum
class Mathematics:
    @classmethod
    def sum(cls, num1, num2):
        return num1 + num2

result = Mathematics.sum(5, 7)
print("Result of addition:", result)