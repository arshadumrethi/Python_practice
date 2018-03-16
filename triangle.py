# def isTriangle(a,b,c):
#     if a + b > c:
#         print "Is a Triangle"
#
#     elif b + c > a:
#         print "Is a Triangle"
#
#     elif a + c > b:
#         print "Is a Triangle"
#
#     else:
#         print "Not a Triangle"
#
# isTriangle(4, 4, 4)

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
