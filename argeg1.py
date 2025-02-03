# example of argument operator 
# we can provide any name in the place of args but we need this * sign 
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5))