import random
import string


#Setting Variables to store alphabets, numbers and symbols.
up_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*()_}{|<>?"


#Setting variable to hold all characters in a pool.
pool = up_letters + low_letters + numbers + symbols

#Ask user how many characters to use, set it to a variable.
n = input("Enter number of chars: ")

#Create function that generates password using using random.
def gen(n):
    print "".join(random.sample(pool, n)) #random.sample takes a second argument specifies how many items to sample.

#Call the function.
gen(n)
