'''
Created on 8 maj 2016

@author: Tohmas
'''
def remove_duplicates_l(l):
    m = []
    [m.append(elem) for elem in l if elem not in m]
    return m

def remove_duplicates_s(l):
    l = set(l)
    return list(l)

l = [1, 2, 4, 1, 5, 2, 4, 6]
print(remove_duplicates_l(l))

print(remove_duplicates_s(l))
