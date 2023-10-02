def format_list(my_list):
    print(", ".join(my_list[0::2]) +" and" ,my_list[-1])

    
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
format_list(my_list)
