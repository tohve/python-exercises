'''
Created on 5 maj 2016

@author: Tohmas
'''
while True:
    number = input("Input a number:")
    if number.isnumeric():
        number = int(number)
        break
    print("That is not a number! Try again!")
    
if (not(number % 4)):
    print(str(number) + " is a multiple of 4")
elif (number % 2):
    print(str(number) + " is an odd number")
else:
    print(str(number) + " is an even number")