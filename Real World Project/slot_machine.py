# Slot machine problem 

# this function spin the row 
def spin_row():
    pass 

def print_row():
    pass 
def pay_out():
    pass 

def main():
    balance=100
    print("************************")
    print("Welcome to Slot Machine")
    print("Symbols:🍒 🍉 🍋 🔔 🌟")
    print("************************")
    while balance > 0:
        print(f"Current Balance is {balance}")

        bet=input("Enter the bet amount\n")

        if not bet.isdigit():
            print("Please enter the valid amount\n")
            continue 

        bet=int(bet)

        if balance < bet:
            print("Insufficient Balance\n")
            continue
        if bet<=0:
            print("Invalid bet amount\n")
            continue

        balance-=bet


    

if __name__=='__main__':
    main()

