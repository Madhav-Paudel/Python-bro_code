# Python Banking Program 


# defining the function 
def show_balance(balance):
    print(f"Your Balance is ${balance:.3f}")

def deposit():
    amount=float(input("Enter the amount you want to deposit\n"))
    if amount<0:
        print("This is not valid money\n")
        return 0
    else:
        return amount
def withdraw(balance):
    amount=float(input("Enter the amount to be withdraw\n"))
    if amount>balance:
        print("You have less balance then the withdraw amount")
        return 0
    elif amount<0:
        print("Amount must not be in Negative")
        return 0
    else:
        return amount 
    

def main():
    balance=0
    is_running=True


    # creating loop 
    while is_running:
        print("Banking Program\n")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit\n")
        choose=input("Enter your choice (1-4)\n")
        
        if choose=='1':
            show_balance(balance)
        elif choose=='2':
            balance+=deposit()
        elif choose=='3':
            balance-=withdraw(balance)
            
        elif choose=='4':
            is_running=False

        else:
            print("Invalid error\n")
        

    print("Have a great day\n")
        

if __name__=='__main__':
    main()

