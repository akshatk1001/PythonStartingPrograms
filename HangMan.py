# importing the random module, which will be used to randomly select a word
import random

# getting the word_list list from the words file in the same folder
from words import word_list

# making the final_word list, which will store the individual letters from the word the player has to guess
final_word = []

# making the player_correct list, which the player will see every time that they guess
player_correct = []

# this list will contain all the letters that the player got wrong
player_wrong = []

def get_word():
    '''
    Computer randomly selects a word from the words.py file
    '''
    rand_word = random.choice(word_list)
    for letter in rand_word:
        final_word.append(letter)
        player_correct.append("_")
    return final_word

def display_hangman(tries):
    '''
    :param tries: the number of incorrect guesses the user has
    :return: how much of the hangman has been drawn so far
    '''
    stages = [
            # initial empty state
            """
               --------
               |      |
               |
               |
               |
               |
               -
            """,

            # head
            """
               --------
               |      |
               |      O
               |
               |
               |
               -
            """,

            # head and torso
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            """,

            # head, torso, and one arm
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            """,

            # head, torso, and both arms
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            """,

            # head, torso, both arms, and one leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,

            # final state: head, torso, both arms, and both legs
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """
    ]
    return stages[tries]

def player_choice():
    '''
    The main loop that the program will run on
    '''
    # having the computer randomly pick a word
    print(get_word())
    player_tries = 0

    while player_correct != final_word and player_tries != 6:
        pl_letter = input("What letter/word do you choose? ")  # asks the player for a letter and stores it
        letter_ind_lst = []  # stores the indexes that the letter the player selects is at (used later)
        if str(pl_letter) in final_word and str(pl_letter) not in player_correct:  # checking if letter is in word and not already guessed
            let_ind = -1  # a starting index. Begin's at -1 as it is iterated to 0 instantly
            for let in final_word:  # for each item in the final_word list
                let_ind += 1  # Setting index to the index of the letter being checked by incrementing by 1
                if let == pl_letter:  # if the letter player selected is the same as the current letter
                    letter_ind_lst.append(let_ind)  # the index of that letter is appended to the letter_in_lst list
            for c_let in letter_ind_lst:  # Put the selected letter into each index value in letter_ind_lst
                player_correct[c_let] = pl_letter
            print("Correct guess! \n")  # tells the guess is right
        elif str(pl_letter) not in final_word and str(pl_letter) not in player_wrong:  # if the letter isn't in word and not already guessed
            player_wrong.append(pl_letter)  # append letter to player_wrong list
            print("Incorrect guess! \n")  # tells guess is wrong
            player_tries += 1
        else:
            print("You have already tried this letter \n")  # only option left is that player has guessed letter already

        print("Correct guesses:", player_correct, "\nIncorrect guesses:", player_wrong) # Prints players' incorrect and correct guesses
        print(display_hangman(player_tries)) # prints the current state of the hangman and how much of it has been drawn

    if player_tries == 6: # If the player has guesses over 6 times, that means the hangman is fully drawn and they lost
        print("You lost! The word was", final_word)


player_choice() # calls the function to run the game.
