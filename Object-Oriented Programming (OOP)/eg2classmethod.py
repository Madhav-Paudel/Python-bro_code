# example of class method 
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
    @classmethod
    def change_increment(cls, amount):
        cls.increment=amount


madhav=Employee('Madhav','Paudel',2500)
print(madhav.salary)
Employee.change_increment(2)
madhav.increase()

print(madhav.salary)
