my_list = [0, 0, 1, 0]

#Join list into string of numbers
a = "".join(str(i) for i in my_list)

#Join list and convert string into integer using int,
#specifying base 2, converts from binary to int
z = int("".join(str(i) for i in my_list), 2)
print a
print z
