numbers = [1, 2, 3]

####### How to remember
###### new_list = [new_item for item in list]

new_list = [n+1 for n in numbers]
print(new_list)

#######   Strings as Lists    ######

name = "Priyanshu"
name_list = [letter for letter in name]
print(name_list)

#######   Making list from range

range_list = [num * 2 for num in range(1, 5)]
print(range_list)


#########      Conditional List Comprehension     ##########

##########   new_list = [new_item for item in list if test]

names = ["Dave", "Amy", "Sheldon", "Alex", "Beth", "Caroline", "Escanor"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)