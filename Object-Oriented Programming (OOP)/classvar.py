# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age



student1=Student("Tek",25)
student2=Student("bipin",20)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
