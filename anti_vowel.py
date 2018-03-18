# Define a function called anti_vowel that takes one string,
# text, as input and returns the text with all of the vowels removed.

def anti_vowel(text):
  word = ""
  for i in text:
    if i not in "aeiouAEIOU":
      word += i
  return word

print anti_vowel("mayuko")
