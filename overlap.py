#This program returns the values that overlap between two lists.

x = [15, 6, 3, 7, 4, 8, 9, 2, 5, 1]

y = [6, 8, 3, 4, 5]

for num in x:
    if num in y:
        print(num)