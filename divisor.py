#This program returns all the values in a range divisible by a given number.

x = range(1, 100)

var = input("Type a number to divide: ")

for num in x:
    if int(var) <= 100 and num % int(var) == 0:
        print(num)

