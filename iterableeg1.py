# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# making list consting number
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number,end=" ")
print(" ")

for number in reversed(numbers):
    print(number,end="-")

# making tuple 
numbers=(1,2,3,4,5,6,7,8,9)
for number in numbers:
    print(number,end=" ")
print(" ")
# for set 
# set are iterable but not reversible 
fruits={"apple","banana","orange","jackfruit"}

for fruit in fruits:
    print(fruit)


# example of string
name="Madhav Paudel"

for character in name:
    print(character,end="")


# example of dictionary 
my_dictionary={"A":1,
               "B":2,
               "C":3,
               "D":4}

for key in my_dictionary.keys():
    print(key)
print(" ")
for value in my_dictionary.values():
    print(value)
print(" ")
for key,value in my_dictionary.items():
    print(f"{key}={value}")
print(" ")
