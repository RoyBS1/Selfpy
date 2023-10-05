def mult_tuple(tuple1, tuple2):
    for i in tuple1:
        for j in tuple2:
            print(i, j)
            print(j,i)

            
first_tuple = (1, 2)
second_tuple = (4, 5)
mult_tuple(first_tuple, second_tuple)
#((1, 4), (4, 1), (1, 5), (5, 1), (2, 4), (4, 2), (2, 5), (5, 2))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
mult_tuple(first_tuple, second_tuple)
