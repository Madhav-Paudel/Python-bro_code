class Employee:
    increment=1.5
    def __init__(self,first,last,pay): #define the constructor 
        self.first=first
        self.last=last
        self.pay=pay 
        self.increment=1.20
    def display(self):
        print(f"{self.first} {self.last}")
        print(f"Salary:{self.pay}")
    def incpay(self):
        self.pay=self.pay*Employee.increment #when we do Employee.increment it the the value inside the 
        #                                     class but when we do self.increment it take the value inside
        #                                     constructor and the code would look like given below
        # self.pay=self.pay*self.increment 

# calling constructor 
emp_1=Employee('Madhav','Paudel',2500)

emp_2=Employee('Teksingh','Tharu',2501485)


emp_1.display()

emp_2.display()

print(emp_1.pay)
emp_1.incpay()
print(emp_1.pay)
# if we want to look the every variable inside the instance it will list all the variable inside the instance 

print(emp_1.__dict__)
# if we want to look the every variable inside the class Employee it will list all the variable inside the instance 
print(Employee.__dict__)
