# Static methods = A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"
    
    # for static method we need decorator 
    @staticmethod
    def is_valid_position(position):
        valid_position=["cook","manager","janitor"]
        return position in valid_position
    
# when we give the item which are at the list then it will print true else it print false
employee1=Employee("Madhav","janitor")
employee2=Employee("Bipin","manager")
employee3=Employee("samir","cook")
print(Employee.is_valid_position("cook"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


