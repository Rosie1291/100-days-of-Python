"""
- Guess a number from 1 - 100:
    result = random range 100
- Choose a difficulty -> set_difficulty()
- Based on the difficulty levels: easy/hard -> users get 5 or 10 guesses
    NUM_OF_GUESS = 5 or 10 (if statement)
- On each guess, user will be suggested if the number's too high or low
    while num_of_guess remains, compare result vs user_guess -> check(user_guess, result, num_of_guess)
- Game ends when user guesses correctly or runs out of attempts
    print statement when win/lose -> game()
"""

import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, result, num_of_guess):
    if user_guess not in range(1, 101):
        print("Please choose a number between 1 and 100.")
        return num_of_guess
    elif user_guess == result:
        return(f"You win! The answer was {result}.")
    elif user_guess < result:
        print(f"Too low.")
        return num_of_guess - 1
    else:
        print(f"Too high.")
        return num_of_guess - 1

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def game():
    print(logo)
    result = random.randint(1,100)
    print(result)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")
    num_of_guess = set_difficulty()

    user_guess = 0
    while user_guess != result:
        print(f"You have {num_of_guess} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        num_of_guess = check_answer(user_guess, result, num_of_guess)
        if num_of_guess == 0:
            return "You've run out of guesses. You lose!"
        elif user_guess != result:
            print("Guess again!")

print(game())