def numbers_letters_count(my_str):
    nums = 0
    chars = 0
    for char in my_str:
        if char.isnumeric():
            nums = nums+1
        elif (char.isalpha or char.isspace):
            chars = chars + 1
    result = [nums, chars]
    print(result)
print(numbers_letters_count("Python 3.6.3"))
