menu = {
    "POP CORN": 1,
    "HOT DOG": 2,
    "GIANT PRETZEL": 2.5,
    "ASST CANTY": 3,
    "SODA": 1.5,
    "WATER BOTTLE": 1,
    "PIZZA": 3.5
}
cart=[]
cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Enter item you need (enter q to quit): ").strip().upper()
    if food.lower() == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not found in menu. Please try again.")

print("-------------YOUR ORDER-------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Total is: ${total:.2f}")
