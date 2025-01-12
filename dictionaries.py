people=[
    {"name":"madhav","number":"9822487602"},
    {"name":"bipin","number":"7892132151"},
    {"name":"ram","number":"798654165654"}
    ]
name=input("enter Name:")
for person in people:
    if person["name"]==name:
        print(f"number is {person['number']}")
        break
else:
    print("not fount!")
    