#Write a function that takes a sequence and returns only the even numbers within it
def purify(x):
    new = []
    for i in x:
        if i % 2 == 0:
            new.append(i)
    return new

#First Solution, it didnt work for all test cases because
#it would stop after the first element or first
#True state was achieved
# def purify(x):
#     for i in x:
#         if i % 2 != 0:
#             x.append(i)
#     return new

print purify([4, 5, 5, 4])
