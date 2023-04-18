"""
1. Higher lower game: user given random data
-> def get_random_account(), def format_account(acc)
2. User guesses who has higher Instagram followers
-> def check_answer
3. Get 1 pt/correct guess, exit if wrong guess (show final score)
-> def game()
4. Each new guess, A becomes B, B gets assigned a new person. Clear screen after every round.
-> def clear
"""

import art
from game_data import data
import os
import random

# function to clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_account():
    return random.choice(data)

def format_acc(acc):
    name = acc['name']
    description = acc['description']
    country = acc['country']
    return f"{name}, a {description}, from {country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    acc_a = get_random_account()
    acc_b = get_random_account()

    while game_should_continue:
        acc_a = acc_b
        acc_b = get_random_account()

        while acc_a == acc_b:
            acc_b = get_random_account()

        print(f"Compare A: {format_acc(acc_a)}.\n{art.versus}\nCompare B: {format_acc(acc_b)}.")
        user_guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()
        a_follow_ct = acc_a["follower_count"]
        b_follow_ct = acc_b["follower_count"]
        is_correct = check_answer(user_guess, a_follow_ct, b_follow_ct)

        clear()
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current scoal: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, you're wrong! Final score: {score}.")

game()
# game done