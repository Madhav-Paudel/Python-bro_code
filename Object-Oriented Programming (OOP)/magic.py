
# Magic methods = Dunder methods (double underscore) _init_, _str_, _eq_
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Student:
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
    def __str__(self):
        return f"{self.name}:{self.gpa}"
    
    def __eq__(self,other):
        return self.name==other.name
    
    def __gt__(self,other):
        return self.gpa >other.gpa
    

student1=Student("Madhav",3.19)
student2=Student("bipin",3.58)
        
print(student1)
print(student2)
print(student1==student2)
print(student1>student2)

