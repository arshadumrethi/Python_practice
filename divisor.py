#A script that takes a number and returns a list of its divisors

def div():
    num = input("Enter a number: ")
    list = []
    for i in range(1, num):
        if num % i == 0:
            list.append(i)
    print list

div()
