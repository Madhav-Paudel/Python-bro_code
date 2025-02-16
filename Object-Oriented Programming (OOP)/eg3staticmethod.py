# example of static method 

class Employee:
    increment=1.5
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.no_of_employees+=1
    def increase(self):
        self.salary=int(self.salary*self.increment)
        # this @ is decorator 
    @classmethod
    def change_increment(cls, amount):
        cls.increment=amount
    # this is decorator for static method
    @staticmethod 
    def isopen(day):
        if day=='sunday':
            return False
        else:
            return True
        


madhav=Employee('Madhav','Paudel',2500)
print(Employee.isopen('sunday')) # this isopen function will work if we do not create object as it is the static funcion of class 
print(madhav.isopen("monday"))
# print(madhav.salary)
# Employee.change_increment(2)
# madhav.increase()

# print(madhav.salary)
