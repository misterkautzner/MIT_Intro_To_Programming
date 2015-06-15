# 6.00 Problem Set 3
# Name: John Kautzner
# Collaborators: None
# Time: 2:15
#
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here! 

def letters_guessed(guess, so_far):
    """
    guess (string): most recent letter guessed

    so_far (string): tuple of letters that have been guessed.
    
    Updates so_far by adding the most recent letter guessed to so_far.
    """

    return so_far + ' ' + guess
    

def in_word(guess, word):
    """
    guess (string) = a single letter (current letter guessed)
    word (string) = the word the player is trying to guess

    determines whether the guessed letter is contained in the word
    
    returns true if the guess is contained in the word
    returns false if the guess is not contained in the word
    """
    guess = guess.lower()
    true = False

    for letter in word:
        if(guess == letter):
            true = True

    return true


def update_info(guess, word, current_info):
    """
    guess (string) = a single letter (current letter guessed)
    word (string) = the word the player is trying to guess

    Replaces blank spaces in current_info with correctly guessed letters

    returns current_info
    """
    guess = guess.lower()

    if(current_info == ''):
        for letter in word:
            current_info += '_ '

    for i in range(0, len(word)):
        if(word[i] == guess):
            current_info = current_info[:i*2] + guess + ' ' + current_info[(i+1)*2:]

    return current_info

word = choose_word(wordlist)        
print "Word selected."
print "The word has", len(word), "letters."

current_word = '' #String containing blank spaces and correctly guess letters
guess = '5'
current_word = update_info(guess, word, current_word) #Initializing current_word
print current_word


so_far = '' #String containing the letters that have been guessed so far
guesses = 6

while(guesses > 0):
    guess = raw_input("Please guess a letter: ")
    print

    so_far = letters_guessed(guess, so_far) #Add letter to list of guessed letters
    print "Letters guessed: ", so_far.upper()

    if(in_word(guess, word)):
        current_word = update_info(guess, word, current_word)
        if(not in_word('_', current_word)):
            break
        
        print "Good guess: ", current_word

    else:
        print "Incorrect: ", current_word
        guesses -= 1

    print "Guesses remaining:", guesses

print
print

if(guesses == 0):
    print 'You lost. The word was:   ', word.upper()

else:
    print 'You won! The word was:', word.upper()

print "Thanks for playing!"
