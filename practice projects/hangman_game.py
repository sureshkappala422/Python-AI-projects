import random # used to pick random fruit
from collections import Counter # counte letters to check of the player guessed the whole word.

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ') #givin words are Convert into a list 

word = random.choice(someWords) #computer picks a random fruite

if __name__ == '__main__':
    print("Guess the word !, Word is a Fruite. ")

    for _ in word:
        print('_', end = ' ') #Show hidden letters and each '_' represents one hidden letter
    print()

    letter_Guessed = '' #stores letter player guessed
    chances = len(word) + 2 # number of tries allowed
    flag = 0 # checks if the player won

    try:
        while chances > 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = input('Enter a latter to Guess: ').lower()
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a letter!')
                continue
            elif len (guess) > 1:
                print('Enter onlay a single letter')
                continue
            elif guess in letter_Guessed:
                print('You already guessed that letter')
                continue

            if guess in word:
                letter_Guessed += guess * word.count(guess)

            for char in word:
                if char in letter_Guessed:
                    print(char, end = ' ')
                else:
                    print('-', end = ' ')

            if Counter(letter_Guessed) == Counter(word):
                print("\nCongratulations! You Guessed the Word: ", word)
                flag = 1
                break
        if chances <= 0 and Counter(letter_Guessed) != Counter(word):
            print('\nYou Lost! The word was: ', word)

    except KeyboardInterrupt:
        print('\nGame Interrupted. Bye!')
        exit            

