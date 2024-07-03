# function1s

'''
fUNCTION NAMED AVERAGE
3 num from user > calculate average


make a function named marks it should take 5 integers as a parameter
print the total
and print the percentage
'''


# def average(num1: int, num2: int, num3: int):
#     average = (num1 + num2 + num3) / 3
#     print(int(average))
#
#
# average(5, 5, 5)


def marks(num1: int, num2: int, num3: int, num4: int, num5: int):
    total = (num1 + num2 + num3 + num4 + num5)
    percentage = (total / 5)
    print(f"total is {total}")
    print(f"percnetage is {percentage}")


marks(15, 60, 70, 80, 90)
