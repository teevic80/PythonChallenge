#This program is a function that returns the first and last values in a list.

prompt = input(("Type in your numbers, separated by a space: "))

x = prompt.split()

def list_ends(first, last):
    return x[0] 
    return x[::-1]

list_ends(5, 6)