print("Please insert a message: ")
message = input()
len1 = round(len(message)/2)

print(message[0:len1].lower(),message[len1::].upper())
