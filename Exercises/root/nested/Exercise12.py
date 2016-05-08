'''
Created on 8 maj 2016

@author: Tohmas
'''

def first_and_last (l):
    x = len(l)
    if x < 2:
        raise ValueError('first_and_last: list must have at least two elements')
    return l[0::len(l)-1]

a = [5, 10, 15, 20, 25]
print(first_and_last(a))

a = [5]
print(first_and_last(a))
