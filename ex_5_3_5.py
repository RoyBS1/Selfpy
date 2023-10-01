def distance(num1, num2, num3):
    if (abs(num3- num1) > 1 or abs(num2 - num1) > 1 ) and (abs(num2 - num3) >= 2 and abs(num2 - num1) >= 2) or (abs(num3 - num2) >= 2 and abs(num3 - num1) >= 2):
        print("True")
    else:
        print("False")
    

distance(1, 2, 10)
distance(4, 5, 3)
