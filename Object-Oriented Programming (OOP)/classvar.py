# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:
    class_year=2024
    no_of_student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # here we are counting the total number of student (object ) are created 
        Student.no_of_student+=1



# here 2 student object is created 
student1=Student("Tek",25)
student2=Student("bipin",20)

print(student1.name)
print(student1.age)
# here class_year is a class variable and it is good practice to access by the name of class 
print(Student.class_year)
print(student2.name)
print(student2.age)
print(Student.class_year)

print(f"the no of object are {Student.no_of_student}")
