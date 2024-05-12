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

# num_char = len(input("What is your name? "))
#
# new_num_char = str(num_char)
#
# print("Your name has " + new_num_char + " characters.")
#
#
# two_digit_number = input()
# # 🚨 Don't change the code above 👆
# ####################################
# # Write your code below this line 👇
#
# num1=int(two_digit_number[0])
# num2=int(two_digit_number[1])
#
# print(num1 + num2)
#
#
# # BMI calculator
#
# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
#
# height_float = float(height)
#
# weight_int = int(weight)
#
# bmi = weight_int / height_float ** 2
#
# print(int(bmi))

##
score = 3
height = 1.8
isWinning = True
score += 1

print(f" your score is {height}, you are wiing by {score}")

age = int(input("age"))
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

years_left = 90 - age

week_left = 52 * years_left

print(f"You have {week_left} weeks left.")


split_bill_Total = input("How much is the bill? ")
split_bill = int(split_bill_Total) / 5
print(split_bill)
each_person_pays = int(split_bill) * 1.12
print(round(each_person_pays, 2))