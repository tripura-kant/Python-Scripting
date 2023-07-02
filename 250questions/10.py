# This is file 10.py
# Given a getSquare() function, make a list comprehension that returns a list with the squares of all even numbers from 0 to 20,
# but ignores those numbers that are divisible by 3.

def getSquare():
    ##Write your code here
    l1 = [x * x for x in range(1, 21) if (x % 2 == 0) and (x % 3 == 0)]  ##Create the list here
    return sum(l1)


print(getSquare())
