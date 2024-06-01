# Functions with input

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid input"
#     print(f_name.title())
#     print(l_name.title())
#
# #format_name("monu", "ttk")
# format_name(" "," ")
# # More functions

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year")
#             else:
#                 print("Not leap year")
#         else:
#             print("Leap year")
#     else:
#         print("Not leap year")
#
#
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("enter year"))  # Enter a year
# month = int(input("enter month"))  # Enter a month
# days = days_in_month(year, month)
# print(days)

#Calculator

#aDD
def add(n1, n2):
    return n1 + n2

#Sub
def sub(n1, n2):
    return n1 - n2

#MUL
def mul(n1, n2):
    return n1 * n2

#DIV
def div(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1 = int(input("what is first number: "))
num2 = int(input("what is sec number: "))

for choosen_sign in operation:
    print(choosen_sign)

operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operation[operation_symbol]
print(calculation_function)
answer = calculation_function(num1, num2)

print(f" {num1} {operation_symbol} {num2} = {answer}")
