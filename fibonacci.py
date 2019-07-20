#This program prints the fibonacci sequence upto a given value.

num = input("Type a number limit for the fibonacci sequence: ")

x, y = 0, 1

while y <= int(num):
    x, y = y, x + y
    print(x)

