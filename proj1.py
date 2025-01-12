# python calculator
operation = input("enter what do you want to perform (+,-,*,/)\n")
a = int(input("enter the number first!\n"))
b = int(input("enter the number second!\n"))

if operation == "+":
    c = a + b
    print(f"the sum of {a} and {b} is {c}")
elif operation == "-":
    c = a - b
    print(f"the subtraction of {a} and {b} is {c}")
elif operation == "*":
    c = a * b
    print(f"the multiplication of {a} and {b} is {c}")
elif operation == "/":
    c = a / b
    print(f"the division of {a} and {b} is {c}")
else:
    print("error 101")