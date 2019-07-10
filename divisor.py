#This program returns all the values divisible by a given number

x = range(1, 100)

input("Type a number.")

for num in x:
    if input <= 100 and num % input == 0:
        print(num)