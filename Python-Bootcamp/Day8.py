# # def greet():
# #     print("Hello")
# #
# #
# # #greet()
# #
# #
# # def greet_with_name(name):
# #     print(f"Hello {name}")
# #
# #
# # greet_with_name("mk12")
#
# # Functions with more than 1 input
#
# # def greet_with(name, location):
# #     print(f"hello {name}")
# #     print(f"    What it is like in {location}")
# #
# # greet_with("monu", "bokaro")
# # greet_with(name="monu122", location="ranchi")
# #
# # greet_with("shilpi", "delhi")
#
#
# # Write your code below this line 👇
# # import math
# #
# #
# # def paint_calc(height, width, cover):
# #     cans = (height * width) / cover
# #     print(f"You'll need {math.ceil(cans)} cans of paint.")
# #
# #
# # # Write your code above this line 👆
# # # Define a function called paint_calc() so the code below works.
# #
# # # 🚨 Don't change the code below 👇
# # test_h = int(input("height  "))  # Height of wall (m)
# # test_w = int(input("width   "))  # Width of wall (m)
# # coverage = 5
# # paint_calc(height=test_h, width=test_w, cover=coverage)
#
#
# ## Prime checker
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("it's not a prime number")
#
# n = int(input("Enter num "))
# prime_checker(number=n)
#

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position =  position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"
encrypt(text=text, shift=3)
##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.