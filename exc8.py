# 2d list in python 
# fruits=["apple","banana","orange"]
# vegetable=["tomato","cabbage","potatoes"]
# meat=["chicken","goat","buffalo"]

groceries=[["apple","banana","orange"],["tomato","cabbage","potatoes"],["chicken","goat","buffalo"]]
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()