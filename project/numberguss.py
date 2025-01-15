# in this program we will create number guessing game 
import random
lowest=1
highest=100
# this generate random number
answer=random.randint(lowest,highest)
# for tracking the number of guess 
T_guess=0
# print(answer)
guess_incorrect=True
print("This is number guessing game")
print(f"Please enter the number between {lowest} and {highest}")
while guess_incorrect:
    value=input("Number:")
    print(f"Your guess amount {T_guess+1}")

    if value.isdigit():
            value=int(value)
            T_guess+=1
            if value== answer:
             guess_incorrect=False
            
            elif value <answer:
                print("Your answer is short by some point")
                print(f"Please enter the number between {lowest} and {highest}")
           
            else:
                print("Your answer is large by some point") 
            
    else:
        print("Invalid input you enter string ")
        print(f"Please enter the number between {lowest} and {highest}")

print(f" You guess is correct the value is {answer}")
print(f"total guess you required is {T_guess}")

