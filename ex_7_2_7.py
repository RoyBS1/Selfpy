def arrow(my_char, max_length):
    for x in range(max_length + 1):
        print(my_char * x)
     
    for x in range(max_length, 0, -1):
        print(my_char * x)

print(arrow('*', 5))
