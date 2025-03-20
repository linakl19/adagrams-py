# comment to practice push to GitHub
from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    total_letter_pool = []
    hand = []

    # create a list with the total amount of letters: 
    for letter, quantity in LETTER_POOL.items():
        total_letter_pool.extend([letter for i in range(quantity)])
    
    # draw 10 random letters from list of letters and append it to the hand
    for i in range(10):
        random_index = randint(0,len(total_letter_pool)-1)
        random_letter = total_letter_pool.pop(random_index)
        hand.append(random_letter)
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass