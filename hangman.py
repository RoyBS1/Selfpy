import re
print("Welcome to the game Hangman")
HANGMAN_ASCII_ART = "HANGMAN"
print(HANGMAN_ASCII_ART)
MAX_TRIES = 6
print("\n")
print("Maximum number of tries is: " + str(MAX_TRIES))

print("Please insert a word:\n")
word = input()
word = word.lower()
print("The word is " + word)
print(re.sub('[a-z]', '_', word))

def is_valid_input(letter_guessed):
    if(len(letter_guessed) > 1) and (not letter_guessed.isalpha()) :
        print("False, from function")
    elif(not letter_guessed.isalpha()):
        print("False, from function")
    elif(len(letter_guessed) > 1):
        print("False, from function")
    else:
        print("True, from function")

print("Guess a letter:")
letter = input()
is_valid_input(letter)

if(len(letter) > 1) and (not letter.isalpha()) :
    print("E3")
elif(not letter.isalpha()):
    print("E2")
elif(len(letter) > 1):
    print("E1")
    
print("The letter is in the word: ")
print(letter in word)
