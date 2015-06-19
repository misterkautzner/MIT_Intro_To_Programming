# 6.00 Problem Set 3B Solutions
#
# Name: John Kautzner
# Collaborators: None
# Time: 0:45
#


from ps3a import *
import time
from perm import *

hand = {'a':2, 'n':1, 't':1, 'o':1, 'm':1, 'y':1}
hand1 = {'r':3, 'u':1, 'b':2, 'e':1, 'x':0}

def len_of_hand(hand):
    """
    Returns the size of the hand
    """

    size = 0
    
    for k in hand:
        size += hand[k]

    return size


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...

    actual_word = []
    len_hand = len_of_hand(hand)
    score = 0
    high_word = ''

    for n in range(1, len_hand + 1):   # Iterating on lengths of words
        for w in get_perms(hand, n):    # Iterating on words of length n
            if(is_valid_word(w, hand, word_list)):  # Returns true for valid words
                actual_word += [w]  # Adds all actual words to a list

    for w in actual_word:
        if(get_word_score(w, len_hand) > score):    # Find the word on the list with the highest score
            score = get_word_score(w, len_hand)
            high_word = w       # Keep the word

    return high_word


#comp_choose_word({'a':1, 'x':2, 'l':3, 'e':1}, 4)

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
