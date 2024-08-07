# Define the list and B
a = [-2, 4, 4, 8, 9]
B = 0

# Find the smallest element greater than or equal to B
max_value = max(a)

# Find the largest element less than or equal to B
min_value = min(a)

# Output the results
print("Smallest element greater than or equal to B:", greater_or_equal)
print("Largest element less than or equal to B:", less_or_equal)


def solve(A, B):
    greater_or_equal = min((x for x in A if x >= B), default=None)

    less_or_equal = max((x for x in A if x <= B), default=None)
    result = [greater_or_equal, less_or_equal, ]

    # print("List with the largest element <= B and smallest element >= B:", result)

    return result
