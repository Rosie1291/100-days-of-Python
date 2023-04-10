"""
- Guess a number from 1 - 100:
    result = random range 100
- Choose a difficulty
- Based on the difficulty levels: easy/hard -> users get 5 or 10 guesses
    num_of_guess = 5 or 10 (if statement)
- On each guess, user will be suggested if the number's too high or low
    while num_of_guess remains, compare result vs user_guess
    print statement: high/low
- Game ends when user guesses correctly or runs out of attempts
    print statement when win/lose
"""

import random
from art import logo

print(logo)

result = random.randint(1,100)
print(result)
difficulty_level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
num_of_guess = 0
if difficulty_level == "easy":
    num_of_guess = 10
elif difficulty_level == "hard":
    num_of_guess = 5

for i in range(num_of_guess):
    user_guess = int(input("Make a guess: "))
    if user_guess not in range(1, 101):
        print("Please choose a number between 1 and 100.")
    elif user_guess == result:
        print(f"You win! The answer was {result}.")
        break
    elif user_guess < result:
        num_of_guess -= 1
        print(f"Too low.\nGuess again.\nYou have {num_of_guess} attempts remaninng to guess the number.")
    else:
        num_of_guess -= 1
        print(f"Too high.\nGuess again.\nYou have {num_of_guess} attempts remaninng to guess the number.")

if num_of_guess == 0:
    print("You've run out of guesses. You lose!")
