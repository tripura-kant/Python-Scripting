# This is file 9.py
# Given an evenSquare() function,
# create a list with the squares of the even numbers from 0 to 20. The final output should be the sum of even numbers in the list:

def evenSquareSum():
    l1 = [x * x for x in range(1, 21) if (x % 2 == 0)]
    return sum(l1)


print(evenSquareSum())
