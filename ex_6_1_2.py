def shift_left(my_list):
    x = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = my_list[2]
    my_list[2] = x
    print(my_list)

    
shift_left([0, 1, 2])
shift_left(['monkey', 2.0, 1])
