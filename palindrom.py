word = input("Enter a word:")
word = word.lower()
word_vice_versa = word[::-1]
if(word == word_vice_versa):
    print("OK")
else:
    print("NOT")
