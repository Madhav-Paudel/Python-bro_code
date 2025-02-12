# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of an object

# creating class 
class car:
    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale

# calling 
car1=car("Tesla",2025,"Black",True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
