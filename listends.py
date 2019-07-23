#This program is a function that returns the first and last values in a list.

prompt = input(("Type in your numbers, separated by a space: "))

x = prompt.split()
y = x[::-1]

def list_ends(first, last):
    print("Your first number is: " + x[0])
    print("Your last number is: " + y[0])

list_ends(x, y)
