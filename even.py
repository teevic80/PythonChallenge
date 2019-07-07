#This program checks if a given value is even or odd.

x = input("Type in a number, ")

if int(x) % 2 == 0:
    print((int(x)), "is even.")

else:
    if int(x) % 2 != 0:
        print((int(x)), "is odd.")

