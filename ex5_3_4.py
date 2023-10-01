def last_early(my_str):
    my_str = my_str.lower()
    char = my_str[-1]
    print(char, my_str[:-1])
    if char in my_str[:-1]:
        print("True \n")
    else:
        print("False \n")
last_early("happy birthday")
last_early("X")
last_early("Wow")
last_early("best of luck")
