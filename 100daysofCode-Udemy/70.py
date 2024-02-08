'''
Design a code which will find whether the given number is Palindrome
number or not.
'''


def is_palindrome(num):
    num_str = str(num)

    reverse_str = num_str[:: -1]

    if num_str == reverse_str:
        print("Number is a palindrome.")
    else:
        print("Number is not a palindrome.")


num = int(input("Enter a num    "))
is_palindrome(num)
