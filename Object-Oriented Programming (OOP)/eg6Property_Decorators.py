# Property Decorators, Setters & Deleters
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
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,given_email):
        self.email=given_email
        


    
if __name__=='__main__':
    madhav=Employee('Madhav','Paudel',25000)
    dikesh=Employee('Dikesh','Sapkota',897)
    print(madhav.email, dikesh.email)
    dikesh.lname='Dangal'
    print(dikesh.email)

