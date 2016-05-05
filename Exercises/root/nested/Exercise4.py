'''
Created on 5 maj 2016

@author: Tohmas
'''
while True:
    number = input("Give me all divisors of (number):")
    if number.isnumeric():
        number = int(number)
        break
    print("That is not a number! Try again!")

l = range(1, number+1)

print([elem for elem in l if not(number % elem)])