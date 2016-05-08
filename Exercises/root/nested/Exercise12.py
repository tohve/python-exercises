'''
Created on 8 maj 2016

@author: Tohmas
'''
a = [5, 10, 15, 20, 25]

def first_and_last (l):
    return l[0::len(l)-1]

print(first_and_last(a))
