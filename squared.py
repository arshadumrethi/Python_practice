def square_digits(num):
    result = ""
    num = str(num)
    for i in num:
        result += str(int(i) ** 2)
    return int(result)




print square_digits(9119)
