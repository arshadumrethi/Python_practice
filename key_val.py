my_dict = {
  "Name": "Guido",
  "Age": 56,
  "BDFL": True,
  "Blood Type": "O Positive"
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]
