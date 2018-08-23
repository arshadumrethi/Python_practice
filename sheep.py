#A function that counts how many sheep(true) are in the array.

# def count_sheeps(array_of_sheeps):
#   count = [0]
#   for True in array_of_sheeps:
#       count += 1
#       print count


array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print array1.count(True)
