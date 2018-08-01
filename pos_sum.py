def positive_sum(arr):
    # Your code here

    # return sum(filter(lambda x: x > 0, arr))

    def neg(arr):
        for i in arr:
            if i > 0:
                return False
        return True

    if neg(arr) == True:
        return 0

    else:
        Z = filter(lambda x: x > 0, arr)
        return sum(Z)






print positive_sum([1,2,3,4,5])
print positive_sum([1,-2,3,4,5])
print positive_sum([-1,2,3,4,-5])
print positive_sum([])
print positive_sum([-1,-2,-3,-4,-5])
print positive_sum([10, 51, 63, 94, 76, -81, -58, 46, -65, -96, -8, -27, 88, -64, -99, 87, 49])
