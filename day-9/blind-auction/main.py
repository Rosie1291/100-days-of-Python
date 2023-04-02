import os
import art


# function to clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.logo)

# Welcome and ask for user's input
print("Welcome to the secret auction program!")

# Initiate dictionary for users' input
bidders = {}

# Program
while True:
    user = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[user] = bid
    next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if next == "yes":
        # call the clear function
        clear()
        continue
    else:
        break

def findWinner(bidders):
    maxBid = 0
    for user,bid in bidders.items():
        if bid > maxBid:
            maxBid = bid
            winner = user
    print("The winner is " + winner + " with a bid of $" + str(maxBid) + ".")

findWinner(bidders)
               

