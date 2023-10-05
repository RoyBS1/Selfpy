import calendar, datetime
my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies":["Sing", "Compose", "Act", "surf"]}
#print(my_dict)
while(True):
    word = input("Please choose an option:")
    if(word == "1"):
        print("Mariah's last name is: ", my_dict["last_name"])
    elif(word == "2"):
        date = my_dict["birth_date"]
        date = date[3:5]
        print("Mariah's month of birth is: ", calendar.month_name[int(date)])
    elif(word == "3"):
        print("Number of Mariah's hobbies:" ,len(my_dict["hobbies"]))
    elif(word == "4"):
        print("Mariah's last hobby is :", my_dict["hobbies"][-1])
    elif(word == "5"):
        my_dict["hobbies"].append("Cooking")
        print("Adding Cooking to Mariah's hobbies: ", my_dict["hobbies"])
    elif(word == "6"):
        date = my_dict["birth_date"]
        day = date[0:2]
        month = date[3:5]
        year = date[6::]
        this_tuple = (day, month, year)
        print(this_tuple)
    elif(word == "7"):
        date = my_dict["birth_date"]
        #date = date[-1:-4]
        mariah_year = date[-4::]
        today = datetime.date.today()
        year = today.year
        print("Mariah's age: ", year - int(mariah_year))
