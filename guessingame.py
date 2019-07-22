#This program lets you guess a name and check if it's the same as the one in the game.

my_guess = ("Orangutan")

prompt = input("Type in your word: ")

while prompt != my_guess:
    print(prompt + " is incorrect.")
    print(input("Type in another word: "))
else:
    if word in guessed == my_guess:
        print("You guessed correctly... You win!" + my_guess + " is the word.")
