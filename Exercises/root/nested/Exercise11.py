'''
Created on 7 maj 2016

@author: Tohmas
'''
from lib2to3.pgen2.token import PERCENT
NOT_PRIME = 0
PRIME = 1

# function for getting an integer with default help text
def get_integer(help_text = "Enter a number: "):

    while True:
        s = input(help_text)
        try:
            n = int(s)
            return n
        except ValueError:
            print("That is not a number! Try again!")

# function for deciding if prime
def is_prime(n):
    
    l = range(2, n)
    l = [elem for elem in l if not n % elem]
    if len(l) == 0:
        return True
    else:
        return False

def get_factors(n):
    r = []
    f = 2
    per = 0
    
    # n even?
    while not n % f:
        n = n / f
        r.append(f)
        
    f = 3
    while n != 1 and f < (n / 2):
        while not n % f:
            n = n / f
            r.append(f)
        f = f + 2
        if int(100*f/n) > per:
            print("%02d" % int(200*f/n), "%", end='\r')
            per = int(100*f/n)

    print("100 %")
    return r

n = get_integer("Give me a possible prime: ")
f = get_factors(n)

if len(f) == 0:
    print(str(n) + " is prime!")
else:
    print(str(n) + " is NOT prime! It is made up of the following primes:")
    [print(str(elem) + " * ", end="") for elem in f[:-1]]
    print(str(f[-1]))
