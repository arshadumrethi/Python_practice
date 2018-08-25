# This program will prompt the user to select a shape,
# then calculate the area of that shape and then
# print the area of that shape to the user

print "***Calculator is starting***"

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Enter Radius: "))
  area = 3.14159 * (radius ** 2)
  print str(area)

elif option == "T":
  base = float(raw_input("Enter Base: "))
  height = float(raw_input("Enter Height: "))
  area = 0.5 * base * height
  print str(area)

else:
  print "Invalid shape entered"

print "****Calculator is shutting down****"
