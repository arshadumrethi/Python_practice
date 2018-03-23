#Python allows for functional programming
#This means you can pass functions as values or variables

lambda x: x % 3 == 0
#is the same as
def by_three(x):
  return x % 3 == 0
#We dont need to give the function a Name
#Hence it is called an anonymous function

#Filter uses the lambda to determine what to filter
#Example

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
#Will print [0,3,6,9,12,15]

#Lambdas are useful when you need a quick function to do some work
#If the function is going to be used repeatedly it is better to use def

#Another Example of Lambda & Filter Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python",languages )

#Another Example
#List of squares of all numbers 1 to 10
squares = [x ** 2 for x in range(1, 11)]

#Print only the squares between 30 and 70
#Primary method: Comparison operator used to write function
print filter(lambda x:30 <= x <= 70, squares)
#A secondary way of writing the function using range
print filter(lambda x:x in range(30, 70), squares)

#Another Example
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)
print message
