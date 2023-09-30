print("Welcome to the game Hangman")
HANGMAN_ASCII_ART = "HANGMAN"
print(HANGMAN_ASCII_ART)
MAX_TRIES = 6
print("\n")
print(MAX_TRIES)

word = "yellow"
print("Guess a letter:")
letter = input()
print(letter)
print(letter in word)