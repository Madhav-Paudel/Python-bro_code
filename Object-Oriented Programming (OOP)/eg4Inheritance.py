# Inheritance Example in python 

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
        
# creating new class which can take the property of Employee 
class Programmer(Employee):
    def __init__(self, fname, lname, salary,prolang,exp):
        super().__init__(fname, lname, salary)
        self.prolang=prolang
        self.exp=exp
    def increase(self):
        self.salary=int(self.salary*self.increment+0.2)
        return self.salary

madhav=Programmer('Madhav','Paudel',25000,'Python','2 month')
print(madhav.fname)
print(madhav.lname)
print(madhav.salary)
print(madhav.prolang)
print(madhav.exp)