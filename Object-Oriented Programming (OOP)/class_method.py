# Class methods = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself.

class Student:
    counter=0
    Total_gpa=0
    # here counter created to track the no. of student created 
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa 
        Student.counter+=1
        Student.Total_gpa+=gpa
        # when the student here the counter is increase by one 
    # instance method
    def get_info(self):
        return f"{self.name}={self.gpa}"
    
    # class method decorator 
    @classmethod
    def get_counter(cls):
        return f"The total student are {cls.counter} and their total gpa is {cls.Total_gpa}"
    # @classmethod
    # def total_gpa(cls):
    #     return f"The "
    @classmethod
    def get_average_gpa(cls):
        if cls.counter==0:
            return 0
        else:
            return f"The average gpa of student is {cls.Total_gpa/cls.counter}"
    
studen1=Student("Bipin",3.40)
student2=Student("Madhav",2.2)
student3=Student("dikesh",3.2)
student4=Student("John",3.92)

print(Student.get_counter())
print(Student.get_average_gpa())
