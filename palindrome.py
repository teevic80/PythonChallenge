#This program returns a string in reverse and checks if it's a palindrome or not.
#A palindrome is a word that has the same letters both backwards and forwards.

pali = input("Type a word: ")

pali_reverse = pali[::-1]

if pali == pali_reverse:
    print(pali_reverse, ": Your word is a Palindrome!!!")
else:
    print(pali_reverse, ": Your word is not a Palindrome.")
