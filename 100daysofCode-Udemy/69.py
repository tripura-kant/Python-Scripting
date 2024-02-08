'''
4. Write a program that accepts a string and calculates the number of letters
and digits.
Suppose if the entered string is: Edureka123
Then the output will be:
LETTERS: - 7
DIGITS: - 3


'''


def cal_str_alpha(input_string):
    letter = 0
    digit = 0

    for char in input_string:
        if char.isalpha():
            letter += 1
        elif char.isdigit():
            digit += 1

    print("letter count: ", letter)
    print("digit count", digit)


input_string = input("Enter a string ")
cal_str_alpha(input_string)
