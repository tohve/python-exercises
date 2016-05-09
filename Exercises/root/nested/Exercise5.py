'''
Created on 6 maj 2016

@author: Tohmas
'''
from random import randint

# Using random lists instead
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Create empty lists
a = []
b = []

# Create one list of lenght 10
for elem in range(0,10):
    a.append(randint(0,99))

# Create an other list of length 20
for elem in range(0,20):
    b.append(randint(0,99))

# Create an emly list where to fill already found items
c = []

# Print generated random lists
print("First list: " + str(a))
print("Second list: " + str(b))

# Find the overlapping items
# Check if an element is in both a and b and not in c and if found add that element to c to avoid duplicates
print("Overlapping items: " + str([elem for elem in a if elem in b and elem not in c and not c.append(elem)]))

# same using sets (exercise 14)
a = set(a)
b = set(b)
print("Overlapping items: " + str([elem for elem in a if elem in b]))
