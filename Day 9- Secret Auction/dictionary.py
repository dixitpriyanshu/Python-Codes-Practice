programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#Retrieving item from dictionary
# print(programming_dictionary["Bug"])

# Adding items to dictionary
programming_dictionary["Loop"] = "The action of doing someting over and over again."
# print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in a computer"
# print(programming_dictionary)


# Lopp through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])