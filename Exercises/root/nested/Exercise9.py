'''
Created on 7 maj 2016

@author: Tohmas
'''
from random import randint

lowest = 1
highest = 9
a = randint(lowest, highest)
n = 0

while True:
    s = input("Guess the number between " + str(lowest) + " and " + str(highest) + " (or type exit): ")
    if s == 'exit':
        break
    
    try:
        guess = int(s)
        if (guess < lowest) or (guess > highest):
            print("Number not within the range, try again!")
            continue
    except ValueError:
        print("Not a number, try again!")
        continue
    
    n = n + 1
            
    if (guess < a):
        print("Too low!")
    elif (guess > a):
        print("Too high!")
    else:
        print("That's rigth! You required " + str(n) + " tries.")
        a = randint(lowest, highest)
        n = 0
        print("Now I have generated a new number!")

print("Thanks for playing!")
