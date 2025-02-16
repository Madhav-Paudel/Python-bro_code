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
    # this __add__ is dunder is method 
    def __add__(self,other):
        return self.salary+other.salary
    # this __add__ is dunder is method 
    def __repr__(self):
        return 'Employee ({}, {}, {})'.format(self.fname, self.lname, self.salary)

madhav=Employee('Madhav','Paudel',25000)
dikesh=Employee('dikesh','sapkota',897)

print(madhav+dikesh)
# when we try to print(madhav+dikesh) without 
# declearing function inside the class then it would not run it would it show error

print(repr(madhav))

