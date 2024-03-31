# create a person class with a class method called instance_count that returns the total number of instances of the class
class Person:
    total_instances = 0

    def __init__(self, name):
        self.name = name
        Person.total_instances += 1

    @classmethod
    def get_total_instances(cls):
        return cls.total_instances

p1 = Person("Patrícia")
p2 = Person("Milena")
p3 = Person("Júlia")

print("Total instances of Person:", Person.get_total_instances())

# create a calculator class with a static method called square that returns the square of a number
class Calculator:
    @staticmethod
    def square(number):
        return number ** 2

result = Calculator.square(5)
print("Square of 5 is:", result)