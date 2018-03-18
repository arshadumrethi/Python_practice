#Write a function that takes a string and returns its reverse
#without using the reversed() function.
def reverse(text):
  rev = ""
  for i in range(len(text), 0, -1): #Reverse range, stepping backwards
    rev += text[i-1] #Appending to text backwards

  return rev

print reverse("abcd")

# First Attempt tried to use .pop() unsuccessfully.  
    # text = list(text)
    # rad = []
    # while len(text) > 0:
    #     rad.append(text.pop())
    #
    # return rad
    #   #r.append(len[text])
    # #print r
