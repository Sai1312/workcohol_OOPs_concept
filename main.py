print("class && object\n")

class car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
        
    def start(self):
        print(f"{self.color} {self.brand} {self.model} started.")
        
brand = input("Enter car brand: ")
color = input("Enter car color: ")
model = input("Enter car model: ")

my_car = car(brand, color, model)
my_car.start()

print("\ninheritances\n")
class ElectricCar(car):  
    def charge(self):
        print(f"{self.brand} {self.color} {self.model} car is getting charged")

brand = input("Enter car brand: ")
color = input("Enter car color: ")
model = input("Enter car model: ")

ecar = ElectricCar(brand, color, model)
ecar.charge()

print("\nencapsulation")

class BankAccount:
    def __init__(self):
        self.current_balance = 10  

    def deposit(self, amount):
        if amount >= 0:
            self.current_balance += amount
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.current_balance

acct = BankAccount()
try:
    deposit_amount = int(input("Enter deposit amount: "))
    if deposit_amount <= 0:
        print("Invalid input amount.")
    else:
        acct.deposit(deposit_amount)
        print(f"Current balance after deposit: {acct.get_balance()}")
except ValueError:
    print("Invalid input. Please enter an amount.")
    
print("\nPolymorphism")

import random
class Bird:
    def sound(self):
        bird_sounds = ["warble", "hoot", "screech", "trill"]
        print(random.choice(bird_sounds)) 

class Dog:
    def sound(self):
        dog_sounds = ["Bark", "Woof", "Grrr", "ruff"]
        print(random.choice(dog_sounds)) 

def animal_sound(animal):
    animal.sound()


user_animal_name = input("Enter an animal (Bird or Dog): ")

if user_animal_name == "bird" or "Bird":
    chosen_animal = Bird()
    animal_sound(chosen_animal)
elif user_animal_name == "dog" or "Dog":
    chosen_animal = Dog()
    animal_sound(chosen_animal)
else:
    print(f"Sorry, I don't know the sound of a '{user_animal_name}'.")
    

print("\nabstraction")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be a positive number.")
        self.side = side

    def area(self):
        return self.side * self.side

try:
    length = int(input("Enter the lenght: "))
    sq = Square(length)
    print(f"The area of the square with side {length} is: {sq.area()}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

