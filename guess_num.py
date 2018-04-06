"""Guess number to win,the computer
 rolls a pair of dice, asks the user to guess a number,
 compares the users guess to the total value, if the users guess is higher
 than the total of the two dices, the user wins, else the computer wins"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter your guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2

  print "The maximum value is %d" %(max_val)
  guess = get_user_guess()

  if guess > max_val:
    print "Guess invalid, the number is too large"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is: %d" %(first_roll)
    sleep(1)
    print "The second roll is: %d" %(second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Result..."
    sleep(1)
    print "The total is: %d" %(total_roll)

    if guess > total_roll:
      print "Yay, you won! GG"
    else:
      print "Whoops, you lose, sorry"

roll_dice(6)
