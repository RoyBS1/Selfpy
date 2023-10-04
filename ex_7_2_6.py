my_list = input("Hi, please inset a shoppint list: \n" )
my_list = my_list.split(",")

answer = 22
while (answer != "9"):
    print("Please choose an option:")
    print("1 - Print the list")
    print("2 - Print number of products in list")
    print("3 - Check if product is in the list")
    print("4 - Check how many times product appears in list")
    print("5 - Delete a product from list")
    print("6 - Add a product from list")
    print("7 - Check if name legal")#TODO
    print("8 - Remove duplicates")#TODO
    print("9 to exit")
    answer = input("please choose an option:")
    
    if answer == "1":
        print(*my_list)
    elif answer == "2":
        print("Number of products in list is ", len(my_list))
    elif answer == "3":
        check_product = input("Please inert product name \n")
        if check_product in my_list:
            print ("Its here")
        else:
            print("Its NOT here")
    elif answer == "4":
        count_product = input("Insert product name \n")
        print(my_list.count(count_product))
    elif answer == "5":
        delete_product = input("Insert product name \n")
        my_list.remove(delete_product)
        print(delete_product, "removed from list")
    elif answer == "6":
        added_product = input("Insert product name \n")
        my_list.append(added_product)
        print(added_product, "was added to list")



        





