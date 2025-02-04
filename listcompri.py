# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]
# using normal for loop
double=[]
for x in range(1,11):
    double.append(x*2)

print(double)
# using list comprehension
# we use this structure in code [expression for value in iterable if condition] 
#  here in expression i use x*2,value =x,iterable=range(1,11)
double=[x*2 for x in range(1,11)]
print(double)

# now we triple the number which are in the list
triple=[x*3 for x in range(1,11)]
print(triple)
# now we are squering number which are in the list
sqr=[x*x for x in range(1,11)]
print(sqr)


# now working with string and converting them in the uppercase 
fruits=["apple","banana","pineapple","orange"]
fruits=[ fruit.upper() for fruit in fruits]
print(fruits)
# ----
fruits_char=[fruit[0] for fruit in fruits]
print(fruits_char)

# storing differnt number in the list
# [expression for value in iterable if condition]
numbers=[-1,-2,-5,7,8,6,4]
positive_num=[ number for number in numbers if number>0 ]
print(positive_num)
negative_num=[ number for number in numbers if number<0 ]
print(negative_num)

