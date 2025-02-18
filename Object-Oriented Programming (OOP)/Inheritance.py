#Inheritance = Allows a class to inherit attributes and methods from another class
#              Helps with code reusability and extensibility
#              class Child(Parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eating (self):
        print(f"{self.name} is eating ")
    
    def sleeping(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print("woof woof")

class Mouse(Animal):
    def speak(self):
        print("che che")

class Cat(Animal):
    def speak(self):
        print("meow meow!")


dog=Dog("blue")
cat=Cat("cool")
mouse=Mouse("mickey")
print("************")
print(dog.name)
print(dog.is_alive)
dog.sleeping()
dog.eating()
dog.bark()
print("************")
print(cat.name)
print(cat.is_alive)
cat.sleeping()
cat.eating()
cat.speak()
print("************")
print(mouse.name)
print(mouse.is_alive)
mouse.sleeping()
mouse.eating()
mouse.speak()