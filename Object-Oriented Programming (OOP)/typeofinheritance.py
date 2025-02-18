# multiple inheritance = inherit from more than one parent class
#                       C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A
class Animal():
    def __init__(self,name):
        self.name=name

    def eating(self):
        print(f"This {self.name} is eating")
    
    def sleeping(self):
        print(f"This {self.name}  is sleeping")

class Pray(Animal):
    def flee(self):
        print(f"This {self.name} is fleeing")

class Predator(Animal):
    def hunt(self) :
        print(f"This {self.name}  is hunting")

class Rabbit(Pray):
    pass 

class Hawk(Predator):
    pass 

class Fish(Pray,Predator):
    pass 


rabbit=Rabbit("test1")

hawk=Hawk("test2")

fish=Fish("test3")

fish.flee()
fish.eating()
# here fish can access both predator and pray class as it can access both class (inherit from both class )
fish.hunt()
fish.sleeping()
# here hawk can only hunt as it have the access of predator class 
hawk.hunt()
hawk.sleeping()
hawk.eating()
rabbit.flee()
rabbit.sleeping()
rabbit.eating()
