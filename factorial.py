# def multiply(a, b):
#     return a * b
#
# def factorial(x):
#     return map(multiply, range(1, x+1))

# def factorial(x):
#     return x * factorial(x - 1)
#     #print n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(5)
