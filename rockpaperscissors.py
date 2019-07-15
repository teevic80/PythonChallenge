#This a simple rock paper scissors game.

import random

game_values = ("Rock", "Paper", "Scissors")

game_start = (input("Welcome to Rock Paper Scissors! Would you like to play? "))


while True:
    if game_start == "yes":
        print(input("Rock, Paper, Scissors?"))
    