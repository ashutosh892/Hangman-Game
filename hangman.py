import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, myword):
    return secret_word == myword

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    letters_left = string.ascii_lowercase
    letters_left=list(letters_left)
    for i in letters_guessed:
        if i in letters_left:
            letters_left.remove(i)
    return "".join(letters_left)

def hangman(secret_word):

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    lives = 8

    letters_guessed = []

    while lives:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if letter in secret_word:
            letters_guessed.append(letter)
            myword= get_guessed_word(secret_word,letters_guessed)
            print("Good guess: {} ".format(myword))
            if is_word_guessed(secret_word, myword) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")

            print(IMAGES[8-lives])
            lives=lives-1
            if lives == 0:
                print("The correct word was : ", secret_word)


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)

