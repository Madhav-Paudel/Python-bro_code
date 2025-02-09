import random
def roll():
    max_value=6
    min_value=1
    roll=random.randint(min_value,max_value)
    return roll
while True:
    player_number=input("enter the number of player(2-4) ")
    if player_number.isdigit():
        players=int(player_number)
        if 2<= players <=4:
            break
        else:
             print("player must between 2-4 player")
    else:
        print("invalid,try again")


max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)<max_score:
    for player_indx in range(players):
        print("\nplayer ", player_indx + 1, " just started\n")
        print("your total score is:", player_scores[player_indx],"\n")
        current_score=0
        while True:
            should_roll=input("would you like to roll (y)?")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                current_score=0
                print("your turn done as you rolled 1!")
                break 
            else:
                current_score+=value
                print("you rolled a: ",value)
                print("your total point is:",current_score)
        player_scores[player_indx]+=current_score
        print("your total score is: ",player_scores[player_indx])
max_score=max(player_scores)
winnig_indx=player_scores.index(max_score)
print("player number ",player_indx+1," is winner with score: ",max_score)