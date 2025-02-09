# weight conveter
weight=float(input("enter your weight"))
unit=input("enter unit (KG or P)")
if unit=="KG":
    weight=weight*2.205
    unit="lbs"
    # print(f"your weight in pound is {weight}")
elif unit=="P":
    weight=weight/2.205
    unit="Kg"
    # print(f"your weight in kg is {weight}")
else:
    print("your unit is invalid {unit}")
print(f"your weight is {weight} {unit}")
