# with open("Day 24 - Working with Files, Directories and Paths/new_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("Day 24 - Working with Files, Directories and Paths/my_file.txt", mode = "a") as file:
#     file.write("\nNew Text.")

####    'w' mode can also create file as new_file.txt is not in the folder

with open("Day 24 - Working with Files, Directories and Paths/new_file.txt", mode = "w") as file:
    file.write("New Text.")