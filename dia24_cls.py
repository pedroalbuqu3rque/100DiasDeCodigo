class ParityChecker:
    @classmethod
    def check_parity(cls, number):   # "cls" refers to the class
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
        
print(ParityChecker.check_parity(5))
print(ParityChecker.check_parity(8))

# password generator
import secrets
import string

class PasswordGenerator:
    def __init__(self, length=12):   # "self" refers to the class instance 
        self.length = length
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters) for _ in range(self.length))
        return password

generator = PasswordGenerator(length=16)
random_password = generator.generate_password()
print("Random Password:", random_password)