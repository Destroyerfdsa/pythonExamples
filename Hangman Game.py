#Hangman game!
#Nicholaus Whites
#11/18
#Hangman

#imports
import random
import time

#constants
HANGMAN = (
"""
______
|     |
|     |
|
|
|
|
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|
|
|
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|     =
|     =
|
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|     =--
|     =
|
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|   --=--
|     =
|
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|   --=--
|     =
|      \\
|
|
|_______
""",
"""
______
|     |
|     |
|     O
|   --=--
|     =
|    / \\
|
|
|_______
""")


MAX_WRONG=len(HANGMAN)-1
WORDS = ("PYTHON","BOOLEAN","FUNCTION","WHILE","TUPLE","LIST","INDEX","FOR","IF","IMPORT")


word = random.choice(WORDS) #word to be guessed
soFar = "-"*len(word) # one dash for each letter in word to be guessed
wrong = 0 # number of wrong guesses player had made
used = [] # letters already guessed

def game():
    global HANGMAN
    global MAX_WRONG
    global WORDS
    global word
    global soFar
    global wrong
    global used

    
    
    print("Welcome to Hangman. Good luck!")

    while wrong < MAX_WRONG and soFar != word:
        print(HANGMAN[wrong])
        print("\nYou've used the following letter:\n",used)
        print("\nSo far, the word is:\n",soFar)

        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()

        while guess in used:
            print("You have already guessed the letter",guess)
            guess = input("Enter your guess: ")
            guess = guess.upper()


        used.append(guess)

        
        if guess == word:
            print("You got the whole word!")
            break

        elif guess in word:
            print("\nYes!",guess,"is in the word!")

            #create new soFar to include guess
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += soFar[i]
            soFar = new
        else:
            print("\nSorry,",guess,"is not in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou have been hanged!")
    else:
        print("\nYou guessed it!")
    print("\nThe word was",word)

    input("\n\nPress the enter key to exit.")
    exit(101)


game()

input("\n\nPress the enter key to exit.")
