def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    if(list1 == list2):
        print("True")
    else:
        print("False")
        
    
list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
are_lists_equal(list1, list2)
are_lists_equal(list1, list3)
