# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method  

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    # getter method for displaying 
    @property
    def width(self):
        return f"{self._width} cm"
        

    @property
    def height(self):
        # here _ sign mean the private 
        return f"{self._height} cm"
    # setting the new value of width  setter method for setting 
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("height must be greater than zero")    
    # using the deleter method is for deleting 
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")



    
            
        


rectangle = Rectangle(3,4)
# we can access private member by using _ sign
print(rectangle.width)
print(rectangle.height)
# here setting the height of the rectangle height 0 to find out 
rectangle.width=0
rectangle.height=0
# here setting the height of the rectangle height 10 to find out 

rectangle.width=10
rectangle.height=10

print(rectangle.width)
print(rectangle.height)
# deleting the rectangle height 
del rectangle.height
del rectangle.width
