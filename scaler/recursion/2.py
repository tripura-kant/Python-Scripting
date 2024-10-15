# import sys
# sys.setrecursionlimit(10**6)
# def print1toA(A):
#     if(A == 0):
#         return
#     print1toA(A - 1)
#     print(A, end = " ")
# class Solution:
#     # @param A : integer
#     def solve(self, A):
#         print1toA(A)
#         print()

# Print A to 1 function

# def printAto1(A):
#     if A == 0:
#         return
#     print(A, end=" ")
#     printAto1(A - 1)
#
#
# A = 10
# printAto1(A)
# print()
# ()


def sum_of_digits(A):
    # Base case: if A is 0, the sum of its digits is 0
    if A == 0:
        return 0
    else:
        # Recursive case: add the last digit to the sum of the remaining digits
        return (A % 10) + sum_of_digits(A // 10)


# Example usage
A = 12345
result = sum_of_digits(A)
print(result)  # This will print 15
