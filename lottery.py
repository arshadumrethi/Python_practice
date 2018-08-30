#The program selects a random number between 1000 & 9999
#The player is asked to input his choice number
#The player is allowed to pick 5 different numbers
#All 5 numbers are compared with the computers choice
#The computer then takes 3 seconds and prints out each second
#Finally the computer prints wether the player has won or lost.

import random
from time import sleep

def rungame():
    compnum = random.randrange(1000, 9999)

    print "Please enter your choices"

    a = input("Enter 1st choice: ")
    b = input("Enter 2nd choice: ")
    c = input("Enter 3rd choice: ")
    d = input("Enter 4th choice: ")

    as_string = str(a) + str(b) + str(c) + str(d)
    as_int = int(str(a) + str(b) + str(c) + str(d))

    print "Your numbers... "
    sleep(2)
    print as_string
    print as_int

    if compnum == as_int:
        print "Goddamn you Won"
    else:
        print "The computer chose: %d" %(compnum)
        sleep(2)
        print "YOU LOSE"

rungame()
