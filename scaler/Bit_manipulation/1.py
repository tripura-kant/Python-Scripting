# A bruteforce solution will be to convert number into base 2 and count number of ones.
#
# Can you think of something better tho? Maybe a solution which runs in O(number_of_ones) atleast. It’s really similar to the trick used to check if a number is a power of 2 in O(1) approx.
#
def count_ones(n):
    count = 0
    while n > 0:
        count += 1
        n = n & (n - 1)  # Turn off the rightmost set bit
    return count


# Example usage:
number = 11  # Binary representation: 11101
print(count_ones(number))  # Output: 4
