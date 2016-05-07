'''
Created on 7 maj 2016

@author: Tohmas
'''
# returns the max of three values
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

# returns the max of n values
def max_of_many(*args):
    n = len(args)
    if n == 0:
        raise NameError('max_of_many: needs at least one arg, none were passed')
    
    largest = args[0]
    for elem in args:
        if elem > largest:
            largest = elem
    return largest

# try'em
print(str(max_of_three(-2, -8, -4)))
print(str(max_of_three('Petter', 'Tohmas', 'Josefin')))

print(str(max_of_many(7, 2, -1, 9, 6, 3)))
print(str(max_of_many('Petter', 'Tohmas', 'Urban', 'Josefin', 'Runar')))

print(str(max_of_many()))
