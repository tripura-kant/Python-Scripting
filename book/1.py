# # This is my first python code
#
# #print('Hello world')
#
#
# for i in range(1,11):
#     print(i)
#     if i == 5:
#         continue

# import sys
# print (len(sys.argv))
#
# print(sys.argv)


# Define a function to find the factors of a number and determine whether each factor is even or odd
def find_factors(n):
    # Create an empty list to store the factors
    factors = []

    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If i divides n evenly, add it to the list of factors
        if n % i == 0:
            factors.append(i)

    # Loop through the list of factors and determine whether each one is even or odd
    for factor in factors:
        if factor % 2 == 0:
            print(factor, "is even.")
        else:
            print(factor, "is odd.")


# Example usage: find the factors of 12 and determine whether each factor is even or odd
find_factors(12)


