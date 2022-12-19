import random
import art
from game_data import data
from replit import clear

first_person = random.choice(data)

is_game_over = False
previous_comparisons = []
score = 0
clear()

while not is_game_over:
    print(art.logo)
    previous_comparisons.append(first_person)
    print(f"Compare A : {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
    print(art.vs)
    second_person = random.choice(data)
    while second_person in previous_comparisons:
        second_person = random.choice(data)
           
    print(f"Against B : {second_person['name']}, a {second_person['description']}, from {second_person['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == "A":
        if first_person['follower_count'] > second_person['follower_count']:
            first_person = second_person
            score +=1
            clear()
        else:
            is_game_over = True
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong, final score {score}")
    elif guess == "B":
        if first_person['follower_count'] < second_person['follower_count']:
            first_person = second_person
            score +=1
            clear()
        else:
            is_game_over = True
            clear()
            print(art.logo)
            print(f"Sorry, that's wrong, final score {score}")        
                