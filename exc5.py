# if else statement 
age=int(input("enter your age:\n"))
if age>=100:
    print("you are too old")
elif age<=18:
    print("you are not qualified ")
elif age<0:
    print("you are not born yet")
else:
    print("you are qualified")