'''
Created on 8 maj 2016

@author: Tohmas
'''
# function for getting an integer with default help text
def get_integer(help_text = "Enter a number: "):

    while True:
        s = input(help_text)
        try:
            n = int(s)
            return n
        except ValueError:
            print("That is not a number! Try again!")

def gen_fib(n):
    l = [1, 1]
    while len(l) < n:
        l.append(l[-1] + l[-2])
    return l[0:n]

n = get_integer("Input how many fibbonacci numbers to generate: ")
print(gen_fib(n))
