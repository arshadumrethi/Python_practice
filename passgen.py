import random
import string

up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*()_}{|<>?"

pool = up_letters + low_letters + numbers + symbols

n = input("Enter number of chars: ")

def gen(n):
    print "".join(random.sample(pool, n))

gen(n)
