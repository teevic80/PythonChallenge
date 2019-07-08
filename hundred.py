#This program asks for users name and age, then returns the year they'll turn 100.

import datetime

date_now = datetime.datetime.now() 

year_today = date_now.year #Returns the current year

print("The year is:", year_today)

name = input("What is your name?")

age = input("What is your current age?")

year_born = year_today - int(age) #Returns the date of birth

print(name, "it looks like you'll be 100 on exactly", year_born + 100 ) 