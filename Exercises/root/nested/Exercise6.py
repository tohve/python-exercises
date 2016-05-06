'''
Created on 6 maj 2016

@author: Tohmas
'''
# get input string
s = input("Input possible palindrome: ")

# reverse it
sb = s[::-1]

if s.lower() == sb.lower():
    print(s + " is a palidrome!")
else:
    print(s + " is NOT a paildrome! Reversing it gives " + sb)
