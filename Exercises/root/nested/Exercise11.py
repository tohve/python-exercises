'''
Created on 7 maj 2016

@author: Tohmas
'''
from datetime import datetime

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
    
    l = range(2, int((n+1)/2))
    l = [elem for elem in l if not n % elem]
    if len(l) == 0:
        return True
    else:
        return False

def get_factors(n):
    o = n
    r = []
    f = 2

    print("Trying to factorize", n)    
    
    # n even?
    while not n % f:
        n = n / f
        r.append(f)
    
    # here n is no longer even just try the lower third
    f = 3
    try_range = int(n / 3) + 1
    
    # factorize using odd values from 3 and upwards
    t = t_start = datetime.now()
    last_print = 0
    while n != 1 and f <= try_range:
        while not n % f:
            # factor found, remove it
            n = int(n / f)
            try_range = int(n / 3) + 1
            r.append(f)
        
        # since n is not even, only try odd factors
        f = f + 2

        # print progress        
        if (f - last_print) > 593713:
            print("Trying", f, end='\r')
            last_print = f
            
    # are there factors, append rest
    if len(r) !=0 and n != 1:
        r.append(int(n))
                        
    # how long didi it take
    d = datetime.now() - t_start
    print("Factorized in", d.seconds, "s")
    
    return r

n = get_integer("Give me a possible prime: ")
f = get_factors(n)

if len(f) == 0:
    print(str(n) + " is prime!")
else:
    print(str(n) + " is NOT prime! It is made up of the following primes:")
    [print(str(elem) + " * ", end="") for elem in f[:-1]]
    print(str(f[-1]))
