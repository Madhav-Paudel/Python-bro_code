# shopping cart program 
foods=[]
prices=[]
total=0
while True:
    food=input("enter food name (press q for exit)\n")
    if food.lower() =="q":
        break
    else:
        price=float(input(f"enter the price of {food}$ "))
        foods.append(food)
        prices.append(price)


print("_-_-_-_-_-_-_-_-_-_-_-_-YOUR CART LIST-_-_-_-_-_-_-_-_-_-_-_-_-")
for food in foods:
    print(food,end=" ")
   
for price in prices:
    total=total+price

print(f"\nthe total price is {total}\n")