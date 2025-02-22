# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

def add_sprinkles(fun):
    def wrapper(*args,**kwargs):
        print("You add sprinklers 🎊")
        # here fun is the base function 
        fun(*args,**kwargs)
    
    return wrapper

def add_fugged(fun):
    def wrapper(*args,**kwargs):
        print("You add fugged 🍫")
        fun(*args,**kwargs)
    return wrapper

# as we call get_ice_cream() function the add sprinkles function automatically get called 
@add_sprinkles
@add_fugged
def get_ice_cream(flavor):
    print(f"Here is your {flavor} flavor ice cream 🍨")


get_ice_cream("mango")

    