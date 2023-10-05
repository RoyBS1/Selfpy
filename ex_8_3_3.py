def count_chars(my_str):
    my_str = my_str.replace(" ", "")
    my_dict = {}
    for i in my_str:
        my_dict[i] = my_dict.get(i,0)+1
    print(my_dict)

    
magic_str = "abra cadabra"
count_chars(magic_str)
#{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
