temp = input("Insert the temperature you would like to convert:")
temp = temp.lower()
if(temp[-1] == "c"):
    print("Temp in F is:")
    new_temp = ((9*int(temp[:-1]))+(32*5))/5
    print(new_temp)
else:
    print("Temp in C is:")
    new_temp = (5*int(temp[:-1])-160)/9
    print(new_temp)
