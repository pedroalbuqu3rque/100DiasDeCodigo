# develop a vehicle class with methods to accelerate and decelerate. create the car and motorcycle classes, inheriting from vehicle and adding specific methods
class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment

    def decelerate(self, decrement):
        self.speed -= decrement


class Car(Vehicle):
    def turn_on_headlights(self):
        return "Headlights turned on!"

class Motorcycle(Vehicle):
    def honk_horn(self):
        return "Horn honked!"

car = Car()
print("Initial speed of the car:", car.speed)
car.accelerate(20)
print("Speed after accelerating:", car.speed)
car.decelerate(5)
print("Speed after decelerating:", car.speed)
print(car.turn_on_headlights())

print()

motorcycle = Motorcycle()
print("Initial speed of the motorcycle:", motorcycle.speed)
motorcycle.accelerate(15)
print("Speed after accelerating:", motorcycle.speed)
motorcycle.decelerate(3)
print("Speed after decelerating:", motorcycle.speed)
print(motorcycle.honk_horn())