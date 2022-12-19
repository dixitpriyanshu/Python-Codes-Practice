import random
from art import logo

number = random.randint(1,100)

print(logo)
print("Welcome to the Number Guessing Game !!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

while guesses != 0:
    print(f"You have {guesses} attempts remaining to guess the number")
    guess = int(input("Make a Guess: "))
    
    if guess == number:
        print(f"You got it, The answer was {number}")
        guesses = 0
    elif guess < number:
        guesses -=1
        print(f"Too low.")
        print("Guess again")
        
    elif guess > number:        
        guesses -=1
        print(f"Too high.")
        print("Guess again")