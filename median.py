#Find the median number from a given sequence.
#The sequence could be in any order and hence it is sorted first
#If the sequence contains an even number of elements, the median
#will be the average of the middle two elements.

def median(x):
    x = sorted(x) #Sort the list into ascending order
    num = x[len(x)/2] #This gets us the first of our middle numbers.
    num2 = x[len(x)/2 - 1] #We subtract one to get the second middle number.

    if len(x) % 2 == 0:
        return (float(num) + num2)/2 #Use float so that the result will be in floating point
    else:
        return x[len(x)/2]

print median([1,2,3,4])
print median([1,2,3,4,5])

# Key learning:
# In the case of decimal point result
# Python will divide and give us a round number
# and store the remainder in memory unless
# the numerator is a floating point number
