# print("Welcome to roalacoaster")
# height = int(input("What is your height in cm "))
#
# if height >= 120:
#     print("You can ride the roalacoaster")
# else:
#     print("You cannot ride")


# Execrcise
#
# numbers=int(input("Enter no "))
#
# if numbers % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
#Multiple if else

# height = int(input("Enter height "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the roalacoster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child ticket worth $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Your ticket is $12 ")
#
#     wants_photo = input("Do you want a photo taken ? Y OR N")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is {bill}")
#
# else:
#     print("Sorry you need to grow older")

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input()  # What size pizza do you want? S, M, or L
#
# if size == "L":
#     bill = 25
#     add_pepperoni = input()  # Do you want pepperoni? Y or N
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "M":
#     bill = 20
#     add_pepperoni = input()  # Do you want pepperoni? Y or N
#     if add_pepperoni == "Y":
#         bill += 3
# elif size == "S":
#     bill = 15
#     add_pepperoni = input()  # Do you want pepperoni? Y or N
#     if add_pepperoni == "Y":
#         bill += 2
#
# add_chesse = input()
# if add_chesse == "Y":
#     bill += 1
#
# print(f"Thank you for choosing Python Pizza Deliveries! \nYour final bill is: ${bill}.")
#
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combine = name1 + name2
#
# lowercase = combine.lower()
#
# t = lowercase.count("t")
# r = lowercase.count("r")
# u = lowercase.count("u")
# e = lowercase.count("e")
#
# first_digit = t + r + u + e
#
#
# l = lowercase.count("l")
# o = lowercase.count("o")
# v = lowercase.count("v")
# e = lowercase.count("e")
# second_digit = l + o + v + e
#
#
#
# score = int(str(first_digit) + str(second_digit))
#
#
#
# if score < 10 or score > 90:
#   print(f"Your score is {score}, you go together like coke and mentos.")
#
# elif 40 <= score <= 50:
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")

# import random
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# import random
# random_num = random.randint(0, 1)
# #print(random_num)
#
# if random_num == 1:
#   print("Heads")
# if random_num == 0:
#   print("Tails")
#
# names = names_string.split(", ")
# # names_string contains the input values provided.
# # The code above converts the input into an array seperating
# # each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random
#
# num_items = len(names)
#
# random_choice = random.randint(0, num_items-1)
#
# print(f"{names[random_choice]} is going to buy the meal today!")

#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)
# print(dirty_dozen[0])
import random
user_choice = int(input("What you want to choose? Type 0 for Rock 1 for paper and 2 for scissor?\n"))

computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice > user_choice:
    print("Younloose")
else:
    print("invalid")