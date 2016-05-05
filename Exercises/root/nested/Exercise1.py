'''
Created on 5 maj 2016

@author: Tohmas
'''
import datetime

name = input("Please enter your name:")

while True:
    age = input("And your age (after your birthday this year):")
    if age.isnumeric():
        age = int(age)
        break
    print("That is not a positive number! Try again!")

while True:
    number = input("Number of printouts:")
    if number.isnumeric():
        number = int(number)
        break
    print("That is not a positive number! Try again!")

now = datetime.datetime.now()

year_of_100th_birthday = str(100 - age + now.year)

if (age < 100):
    print((name + ", you will be 100 years in year " + year_of_100th_birthday + "\n") * number)
elif (age == 100):
    print((name + ", congratulations! Current year, " + year_of_100th_birthday + ", is the year of your 100th birthday!\n") * number)
else:
    print((name + ", congratulations! You became 100 years back in " + year_of_100th_birthday + "\n") * number)