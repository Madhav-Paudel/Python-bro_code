string="NEPAL"
counter=0
# converting string character into list by using list comprehension 
my_list=[x for x in string]
print(my_list)
# number of guess 
x=5 

while counter!=5:
    user_str=input("enter letter:\n",).upper()
    x-=1
    # reducing guess 
    if user_str in my_list:
        counter+=1
        my_list.remove(user_str)
        print(my_list)
        print("Your guess is correct!😊")
        
    if 0==len(my_list):
        print("😎 you won 🎉")
        break 
    
    if x==0:
        print("You lose ❌" )
        break
    print(f"you have {x} guess remain")
    
print(counter)