'''
Created on 5 maj 2016

@author: Tohmas
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

while True:
    largestNumber = input("Print only numbers less than:")
    if largestNumber.isnumeric():
        largestNumber = int(largestNumber)
        break
    print("That is not a number! Try again!")
    
for element in a:
    if (element < largestNumber):
        b.append(element)
print(b)

print([element for element in a if element < largestNumber])
