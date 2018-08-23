
#A function that takes 3 inputs and determines if they can form a triangle

a=input()
b=input()
c=input()

def tri():
    if a + b > c:
        print "Is a Triangle"

    elif b + c > a:
        print "Is a Triangle"

    elif a + c > b:
        print "Is a Triangle"

    else:
        print "Not a Triangle"

tri()
