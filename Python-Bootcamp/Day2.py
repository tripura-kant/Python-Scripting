# Data Types

#
# # String
#
# print("HELLO"[3])
# print("123" + "234")
#
#
# #String
#
# print(123 + 345)

num_char = len(input("What is your name? "))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")


two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

num1=int(two_digit_number[0])
num2=int(two_digit_number[1])

print(num1 + num2)