#This a simple rock paper scissors game.

import random

game_values = ("Rock", "Paper", "Scissors")

game_start = (input("Rock Paper Scissors! Would you like to play? "))


while True:
    if game_start == "yes":
        yes_game = input("Rock, Paper, Scissors? ")
        print("My Choice is...")
        print(random.choice(game_values))
    else:
        if game_start == "no":
            print("Game Closed")
            break
        else:
            print("Your input is invalid")

# if yes_game == "Rock" and     
        
# 
    #     else:
    #         print("Your input is invalid.")      
    # else:
    #     print
    #     break
    
