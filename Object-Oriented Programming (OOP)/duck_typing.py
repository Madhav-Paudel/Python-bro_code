# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                 Object must have the minimum necessary attributes/methods
#                "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("wof wof")
    
class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    # def honk(self): here car is not taking the character of 
    # animal it is taking from animal as it is speaking 
    alive=False
    def speak(self):
        print("HONK!")

animals=[Dog(),Cat(),Car()]


for animal in animals:
    animal.speak()
    print(f"This is living thing is it true. {animal.alive}")

