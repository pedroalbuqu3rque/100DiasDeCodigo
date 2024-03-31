# modeling
class People:
    def __init__(self, name, age, cpf):   # initialize an object's attributes
        self.name = name   # "self" reference an instance
        self.age = age
        self.cpf = cpf

    def enter_system(self):
        print(f"{self.name} is entering the system...")

p1 = People('João Santos', 21, '123.456.789-00')
p2 = People('Ana Araújo', 23, '987.654.321-00')

p1.enter_system()
p2.enter_system()

# constructor method
class Customers:
    def __init__(self, name, age, cpf):
        print(f'{name} | {age} | {cpf}')

    def purchase_confirmation(self):
        print(f'A purchase has been completed.')

p1 = Customers('Carlos Nascimento', 21, '777.888.999-00')