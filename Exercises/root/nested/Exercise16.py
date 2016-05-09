'''
Created on 9 maj 2016

@author: Tohmas
'''
words = list("My Pass Better Come Back From Analog Time".split())
from random import randint

def main():
    
    while True:
        s = input("Select strength (w)eak, (m)edium, (s)trong or (q)uit: ")
        
        if s == "q":
            break
        
        p = []
        if s == "w":
            print("A lousy password:")
            p = [words[randint(0,7)], words[randint(0,7)]]
        elif s == "m":
            print("Here comes a rather good password:")
            while len(p) < 6:
                p.append(chr(randint(97,122)))
        elif s == "s":
            print("Here comes a good strong password:")
            while len(p) < 12:
                p.append(chr(randint(33,126)))
        else:
            print("Erroneous selection, try again!")
            continue
        
        print(''.join(p))
    
main()
    