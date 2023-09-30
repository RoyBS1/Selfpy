import re
print("Welcome to the game Hangman")
HANGMAN_ASCII_ART = "HANGMAN"
print(HANGMAN_ASCII_ART)
MAX_TRIES = 6
print("\n")
print(MAX_TRIES)

word = input()
word = word.lower()
print(word)
print(re.sub('[a-z]', '_', word))

print("Guess a letter:")
letter = input()
print(letter in word)
