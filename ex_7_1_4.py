def squared_numbers(start, stop):
    nums = []
    while(start <= stop):
        nums.append(pow(start, 2))
        start += 1
    print(nums)
    
squared_numbers(4, 8)
squared_numbers(-3, 3)
