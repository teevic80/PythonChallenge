#This program returns all the values divisible by a given number

x = range(1, 100)

var = input("Type a number: ")

for num in x:
    if num in var < 100 and num % var == 0:
        print(num)