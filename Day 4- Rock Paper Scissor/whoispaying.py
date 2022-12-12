
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# random_choice = random.randint(0,len(names)-1)
# person = names[random_choice]

person = random.choice(names)

print(f"{person} is going to buy the meal today!")