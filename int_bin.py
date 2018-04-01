#int function has an optional second parameter.
#When given a string containing a number and the base that number is in,
#the function will return the value of that number converted to base ten.

int("42")
# ==> 42

int("110", 2)
# ==> 6

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)

print int("11001001", 2)
