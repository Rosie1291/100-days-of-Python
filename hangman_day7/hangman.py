import random
import hangman_art
import hangman_words

print(hangman_art.logo)

# Generate a random word
word_chosen = random.choice(hangman_words.word_list)
print('The secret word: ' + word_chosen)

# Create an array to hint user about the word
display =[]
for letter in word_chosen:
    display += '_'

end_of_game = False
lives = 6
while not end_of_game:
    # Ask user to guess a letter
    guess = input('Guess a letter: ').lower()
    # Check the guessed letter
    if guess in display:
        print(f"You already guessed the letter '{guess}'.")

    # Update the display with the guessed letter   
    for pos in range(len(word_chosen)):
        if guess == word_chosen[pos]:
            display[pos] = word_chosen[pos]

    # Terminate a life if incorrect guess
    if guess not in word_chosen:
        lives -= 1
        print("The letter you guessed is incorrect.")
        if lives == 0:
            end_of_game = True
            print('You lose!')

    # Print the display
    print(''.join(display))

    # Print the ASCII in correspond to the lives user has left
    print(hangman_art.stages[lives])

    if '_' not in display:
        end_of_game = True
        print('You win!')
