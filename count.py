#Write a function to return the number of occurences
#of a particular item in a list.
def count(sequence, item):
  num = 0
  for i in sequence:
      if item == i:
          num += 1
  return num
     

print count([1, 2, 1, 1], 1)
