# A basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:
#
# View the calendar
# Add an event to the calendar
# Update an existing event
# Delete an existing event
# The program should behave in the following way:
#
# Print a welcome message to the user
# Prompt the user to view, add, update, or delete an event on the calendar
# Depending on the user's input: view, add, update, or delete an event on the calendar
# The program should never terminate unless the user decides to exit

from time import sleep, strftime

name = "Arshad"

calendar = {}

def welcome():
  print "Welcome " + name + "."
  print "The calendar is opening..."
  sleep(1) #Adds a second before printing the next line.
  print "Today is: " + strftime("%A %B %d, %Y")
  print "The time is: " + strftime("%H %m %S")
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True

  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit :")
    if user_choice == "V":

      if len(calendar.keys()) < 1:
        print "Calendar is empty"
      else:
        print calendar

    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter update: ")
      calendar[date] = update
      print "Update Successful"
      print calendar

    elif user_choice =="A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")

      if len(date) > 10: #or date[6:1] < strftime("%Y"):
        print "Invalid Date entered"
      	try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()

        if try_again == "Y":
          continue
        else:
          start = False

      else:
        calendar[date] = event
        print calendar

    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar Empty"

      else:
        event = raw_input("What Event?: ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event deleted"
            print calendar
          else:
            print "Incorrect event specified"
    elif user_choice == "X":
      start = False

    else:
      print "Invalid command entered"
      start = False


start_calendar()
