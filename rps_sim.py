"""Rock
Paper
Scissors"""

from random import randint


options = ["ROCK", "PAPER", "SCISSORS"]

message = {"tie":"Yawn it's a tie!",
          "won":"Yay you won!",
          "lost":"Aww you lost!"}

def decide_winner(user_choice, computer_choice):
  print user_choice
  print computer_choice

  if user_choice == computer_choice:
    print message["tie"]

  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]

  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]

  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]

  else:
      print message["lost"]

def play_rps():
    #print "Rock, Paper or Scissors?"
    user_choice = options[randint(0, 2)]
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    return decide_winner(user_choice, computer_choice)

play_rps()
