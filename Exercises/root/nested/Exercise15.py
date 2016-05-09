'''
Created on 9 maj 2016

@author: Tohmas
'''
def reverse_words():
    s = input("Write a sentence to reverse:")
    
    l = s.split(" ")
    l = l[::-1]
    
    print(l)
    
reverse_words()