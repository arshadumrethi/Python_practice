#List Comprehension syntax is used to build lists easily

#Example 1
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print even_squares

#Example 2
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print cubes_by_four

#Example 3
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

#List Slicing is used if only want part of the list
#List Slicing Syntax [start:end:stride]
#Example
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]

# Omitting Indices
# If you don't pass a particular index to the list slice,
# Python will pick a default.
to_five = ['A', 'B', 'C', 'D', 'E']

print to_five[3:]
# prints ['D', 'E']

print to_five[:2]
# prints ['A', 'B']

print to_five[::2]
# prints ['A', 'C', 'E']

my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]

#A negative stride progresses through the list from right to left.
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
backwards = my_list[::-1]
print backwards

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

#Another Example
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message
