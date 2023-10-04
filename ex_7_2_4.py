def seven_boom(end_number):
    for x in range(0, end_number):
        if(x%7 == 0 or '7' in str(x) ):
            print("BOOM")
        else:
            print(x)
            
print(seven_boom(19))
