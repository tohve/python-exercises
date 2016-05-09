'''
Created on 9 maj 2016

@author: Tohmas
'''
import string
import random

def password_gen(size = 8, c=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(c) for _ in range(size))

print(password_gen(int(input("Generate a password of size: "))))
