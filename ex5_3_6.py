def filter_teens(a = 13, b = 13, c = 13):
    #print(a,b,c)
    if(a >= 13 and a <=19 and a != 15 and a != 16):
        a = fix_age(a)
        #print("Value in filter teens = " + str(a))
    if (b >= 13 and b <=19 and b != 15 and b != 16):
        b = fix_age(b)
        #print("Value in filter teens = " + str(b))
    if (c >= 13 and c <=19 and c != 15 and c != 16):
        c = fix_age(c)
        #print("Value in filter teens = " + str(c))
        
    result = a+b+c
    print(result)
    
def fix_age(age):
    age = 0
    #print("Value in fixage = " + str(age))
    return age
    

filter_teens()
filter_teens(1, 2, 3)
filter_teens(2, 13, 1)
filter_teens(2, 1, 15)
