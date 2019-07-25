prompt = input("Type a number: ")

def odd_number(n):
    for i in range(0, n):
        if i % 2 != 0:
            print(i)

odd_number(6)
