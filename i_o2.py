#When we use With As we done need to call close() because __exit__() built in function takes care of it
with open("text.txt", "w") as my_file:
  my_file.write("Yay!")

if my_file.closed == False:
  my_file.close()

print my_file.closed
