'''
Created on 9 maj 2016

@author: Tohmas
'''
def reverse_words():
    s = input("Write a sentence to reverse: ")
    
    l = s.split()
    l = l[::-1]
    
    print(' '.join(l))
    
reverse_words()