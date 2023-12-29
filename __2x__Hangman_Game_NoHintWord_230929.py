
import random

#importing logo:
print("Welcome to:")
from __2x__Hangman_logo_230929 import logo
print(logo)

#importing 6stages:
from __2x__Hangman_6Stages_230929 import stage


#importing word list:
from __2x__Hangman_FullWordList_230929 import word_list


# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)

# Ask the user to guess a letter and convert it to lowercase (input already in the while loop below)


# Deconstruct the chosen word into a list of characters.
deconstructed_chosen_word = list(chosen_word)

# Initialize the board with underscores.
l = len(chosen_word)
#you can use display instead of board if you want
board = ["_"] * l
#print(f"The current board: {board}")

# Display the current state of the board.
#print(' '.join(board))

# Step 2


lives_left = 6

end_of_game = False

while not end_of_game:
    if "_" not in board:
        end_of_game = True
        print("You won!!!!!")
        break

    guess = input("Please make a guess of a letter you think may be inside the word! : \n").lower()

# Update the board based on the new guess.
    for position_on_board in range(l):
        # Display the updated state of the board.

        if guess == deconstructed_chosen_word[position_on_board]:
            board[position_on_board] = guess
    print(' '.join(board))
    if guess in deconstructed_chosen_word:
        print(f"Nice work! You guessed a correct letter! You chose '{guess}'")
    else:
        lives_left -= 1
        print(f"Sorry, but '{guess}' was not in this index place. 1 Life Lost! You have {lives_left} lives left.\n")
        print(f"{stage[lives_left]}")
        if lives_left == 0:
            print("You did not guess in time. Sorry, you lose! Try again!")
            break
else:
    print("You did not guess in time. Sorry, you lose! Try again!")

# Display the updated state of the board.
print(' '.join(board))

#User_Wins