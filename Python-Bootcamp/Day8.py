# def greet():
#     print("Hello")
#
#
# #greet()
#
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#
#
# greet_with_name("mk12")

# Functions with more than 1 input

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"    What it is like in {location}")
#
# greet_with("monu", "bokaro")
# greet_with(name="monu122", location="ranchi")
#
# greet_with("shilpi", "delhi")


# Write your code below this line 👇
# import math
#
#
# def paint_calc(height, width, cover):
#     cans = (height * width) / cover
#     print(f"You'll need {math.ceil(cans)} cans of paint.")
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("height  "))  # Height of wall (m)
# test_w = int(input("width   "))  # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


## Prime checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("it's not a prime number")

n = int(input("Enter num "))
prime_checker(number=n)