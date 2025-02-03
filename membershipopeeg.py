# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in
# this is for the string or for the example of string
word ="APPLE"
letter=input("enter the word for guessing \n")
# here in and not in are boolean return type data type 
if letter in word:
    print(f"yes it contain letter {letter}\n",end=" ")
else:
    print(f"No it contain letter {letter}\n",end=" ")


# example of set
students={"madhav","bipin","sanskar","roman","john","dikesh","samir"}

name=input("enter the name of search in the list\n")

if name in students:
    print(f"{name} is in the list\n")
else:
    print(f"{name} is not in the list\n")

# example of dictionary 
grades={"madhav":"B",
        "bipin":"A",
        "sankar":"B+",
        "roman":"A+"}

name=input("enter the name of student\n")

if name in grades:
    print(f"{name} get {grades[name]} grade\n")
else:
    print(f"{name} not found ")

# using membership operator to verify valid email or not 
email="madhavpaudel40400@gamil.com"
if "@gamil" in email and "." in email:
    print(f"{email}\n is valid email\n")
else:
    print(f"{email}\n is not valid email\n")
