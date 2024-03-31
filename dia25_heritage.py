class Person:   # base class

    def speak(self):
        print("I'm speaking")

    def walk(self):
        print("I'm walking")

class Customer(Person):   # inherited from person. customer is a person
    
    def buy(self):
        print("I'm buying")

class Seller(Person):

    def speak(self):
        super().speak()   # references the base class
        print("I'm screaming")   # overlay, the order of execution is first from "child class" to "parent class" / base class

    def sell(self):
        print("I'm selling")

s1 = Seller()
s1.speak()
s1.walk()
s1.sell()

# method override
class Person:
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

class Customer(Person):
    def __init__(self, id_customer, name, cpf):
        super().__init__(name, cpf)
        self.id_customer = id_customer

c1 = Customer(2, "Albus", "123.456.789-00")
print(c1.id_customer)
print(c1.name)
print(c1.cpf)

# multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking.")


class Feline(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

    def jump(self):
        print(f"{self.name} is jumping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

    def run(self):
        print(f"{self.name} is running.")


class Cat(Feline):
    pass   # inherits meow and jump from the Feline class


class Lynx(Feline):
    def roar(self):
        print(f"{self.name} is roaring.")


class GermanShepherd(Dog):   
    pass 

cat = Cat("Tom")
cat.meow()
cat.jump()
cat.walk()

lynx = Lynx("Leo")
lynx.roar()
lynx.walk()

german_shepherd = GermanShepherd("Loki")
german_shepherd.bark()
german_shepherd.run()
german_shepherd.walk()