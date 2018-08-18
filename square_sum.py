#Function returns the sum of the squares of each number in numbers.
def square_sum(numbers):
    count = 0
    for i in numbers:
        count += i*i
    return count

square_sum([1, 2, 3])
