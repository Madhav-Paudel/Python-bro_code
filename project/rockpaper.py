# rock paper scissor game
import random
options =("rock","paper","scissor")
running=True 
while running:
    
    player=None
    computer=random.choice(options)


    while player not in options:
        player=input("enter a choice (rock , paper, scissor)")

    print(f"Player: {player}")
    print(f"Computer:{computer}")


    if player==computer:
        print("Tie ????")
    elif player=="rock" and computer=="scissor":
        print("You win !!")
    elif player=="rock" and computer=="paper":
        print("Computer won!!")
    elif player=="paper" and computer=="scissor":
        print("Computer won!!")
    elif player=="paper" and computer=="rock":
        print("You win!!")
    elif player=="scissor" and computer=="paper":
        print("You win!!")
    elif player=="scissor" and computer=="rock":
        print("Computer won!!")
    else:
        print("you lose")
    if not input("enter y for play again ").lower()=="y":
        running=False

print("thanks for playing")

