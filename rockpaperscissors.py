#This a simple rock paper scissors game.

import random

# game_values = ("Rock", "Paper", "Scissors")

# game_start = (input("Rock Paper Scissors! Would you like to play? "))


# while True:
#     if game_start == "yes":
#         yes_game = input("Rock, Paper, Scissors? ")
#         print("My Choice is...")
#         mine = print(random.choice(game_values))
#     else:
#         if game_start == "no":
#             print("Game Closed")
#             break
#         else:
#             print("Your input is invalid")

#     if mine == yes_game:
#         print("We've Tied")

#     if mine == "rock" and yes_game == input("paper"):
#         print ("You've won this round.")
#     else:
#         print ("You loose this round.")

#     if mine == "scissors" and yes_game == "rock":
#         print ("You've won this round.")
#     else:
#         print ("You loose this round")

#     if mine == "paper" and yes_game == "scissors":
#         print ("You've lost this round")
#     else:
#         print ("You've won this round")


outcomes = ("Rocks", "Paper", "Scissors")

def to_play():
    input("Would you like to play? ")
    while True:
        input("Rock, Paper, Scissors? ")
    else:
        print("Closing Game.....  Game CLOSED")


to_play()

print(random.choice(outcomes))