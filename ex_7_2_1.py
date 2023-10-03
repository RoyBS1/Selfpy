def is_greater(my_list, n):
    nums = []
    for num in my_list:
        if num > n:
            nums.append(num)
    return(nums)
        
    '''
    for num in my_list:
        print("num is: " + str(num), "n is: "+ str(n))
        if n >= num:
            my_list.remove(num)
    return my_list
    '''
    
result = is_greater([1, 30, 25, 60, 27, 28], 28)
print(result)
