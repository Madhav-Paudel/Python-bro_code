# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    def describe(self):
        print(f"The shape of color is {self.color} and is {'filled' if self.is_filled  else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
    def describe(self):
        # here we do method overwriting as we making the same function which is at the super class or at parents class 

        print(f"The area of circle is {3.14*self.radius*self.radius} cm^2")
        super().describe()


class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width
    def describe(self):
        # here we do method overwriting as we making the same function which is at the super class or at parents class 
        print(f"The area of Square is {self.width*self.width} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
    def describe(self):
        # here we do method overwriting as we making the same function which is at the super class or at parents class 
        print(f"The area of Square is {self.width*self.height} cm^2")
        super().describe()



# calling constructor
circle=Circle("Red",True,5)
print("Details of circle")
print(circle.color)
print(circle.is_filled)
print(circle.radius)
square=Square(color="Blue",is_filled=False,width=55)
print(f"The color of square is {square.color} and the square is filed it is{square.is_filled}.The width of square is {square.width} cm")
triangle=Triangle(color="Black",is_filled=False,width=52,height=78)

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()
circle.describe()
square.describe()



