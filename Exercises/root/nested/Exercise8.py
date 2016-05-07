'''
Created on 7 maj 2016

@author: Tohmas
'''
from random import randint

rps = ['rock', 'paper', 'scissors', 'quit', 'r', 'p', 's', 'q']

while True:
    # get user input
    s = ''
    while s not in rps:
        s = input("Input rock, paper or scissors (or quit): ")
        if s not in rps:
            print("Invalid input, try again!")
    
    # get first letter
    s = s[0]
    
    # does the user want to quit?
    if s == 'q':
        break
    
    # generate computer choice
    sc = rps[randint(0,2)]
    print("Computer said " + sc)
    
    # calculate winner
    if (s == 'r') & (sc == 'scissors'):
        print("You win!")
    elif (s == 'p') & (sc == 'rock'):
        print("You win!")
    elif (s == 's') & (sc == 'paper'):
        print("You win!")
    elif s == sc[0]:
        print("It's a tie!")
    else:
        print("You lose!")

print("Thanks for playing!")