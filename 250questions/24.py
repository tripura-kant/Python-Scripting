# This is file 24.py

def printEvenOdd(n):
    while (n > 0):
        if (n % 2 == 0):
            print("Even number:", n)
        else:
            print("Odd number:", n)
        n = n - 1


print(printEvenOdd(5))
