#Add the digits of a given integer

def digit_sum(x):
    digits = str(x) #Convert to string for iteration
    total = 0
    for i in digits:
        total += int(i) #Convert each digit individually back to integer to store and add them
    return total

    #Other possible Solution
    #num = map(int, str(x))
    #print sum(num)

    #First Idea
    # for i in num:
    #   digits = num.split()
    # return sum(digits)

print digit_sum(434)
