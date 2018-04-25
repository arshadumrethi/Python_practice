my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

#Writing to a file
for item in my_list:
  my_file.write(str(item) + "\n")
my_file.close()

#Reading from a file 
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()
