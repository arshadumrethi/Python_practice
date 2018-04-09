#Function that takes a list of numbers and outputs the largest value without using
#in-built max() function

def largestnumber(a):
    num = a[0]
    for i in a:
        if num < i:
            num = i
    return num

print largestnumber([77,48,19,17,93,90])

# def highestNumber(l):
#     myMax = l[0]
#     for num in l:
#         if myMax < num:
#             myMax = num
#     return myMax
#
#
# print highestNumber ([77,48,19,17,93,90])
