#Write a function that replaces the specified word in text with asterisks
def censor(text, word):
    text = text.replace(word,"*" * len(wrd))
    return text



# First attempt
  # num = len(word)
  # t1 = text.split()
  # for i in t1:
  #   if i == word:
  #     word = "*" * num
  # return "".join(t1)


#Used this code snippet to learn how to use str.replace()
# st = "this is string example....wow!!! this is really string"
# print st.replace("is", "was")
# print st.replace("is", "was", 3)
