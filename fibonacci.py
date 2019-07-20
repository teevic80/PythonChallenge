#This program prints the fibonacci sequence.

x, y = 0, 1

while y <= 1000:
    x, y = y, x + y
    print(x)

