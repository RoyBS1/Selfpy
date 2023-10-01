def func(num1, num2):
    '''This function gets 2 parameters - day and a month 
    and translate it to months from numbers.
    The return value is date withou year'''
    
    day = num1
    month = "month"
    if num2 == 1:
        month = "Jan"
    elif num2 == 2:
        month = "Feb"
    elif num2 == 3:
        month = "Mar"
    elif num2 == 4:
        month = "Apr"
    elif num2 == 5:
        month = "May"
    elif num2 == 6:
        month = "Jun"
    elif num2 == 7:
        month = "Jul"
    elif num2 == 8:
        month = "Aug"
    elif num2 == 9:
        month = "Sep"
    elif num2 == 10:
        month = "Oct"
    elif num2 == 11:
        month = "Nov"
    else:
        month = "Dec"
    
    print("The date is: " + str(month) ,day)
def main():
    func(30, 5)
    help(func)

if __name__ == "__main__":
    main()
