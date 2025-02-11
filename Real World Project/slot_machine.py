# Slot machine problem 
import random

# this function spin the row 
def spin_row():
    symbols=['🍒','🍉','🍋','🔔','🌟']
    return [random.choice(symbols) for _ in range(3)]



def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def pay_out(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet *3
        elif row[0]=='🍉':
            return bet *4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*6
        else:
            return bet*10
    return 0


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
        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=pay_out(row,bet)
        if payout>0:
            print(f"You won the bet {payout}")
        else:
            print("You lose the Bet")
        
        balance+=payout

        var=input("Do You want to play again ? (Y/N) \n").lower()
        if var!='y':
            break
    print("***************************************")
    print(f"Game Over! Your Balance is {balance}")
    print("****************************************")

if __name__=='__main__':
    main()

