def min_time_to_equal_elements(A):
    max_value = A[0]
    for num in A:
        if num > max_value:
            max_value = num

    total_time = 0
    for num in A:
        total_time += max_value - num
    return total_time


# Example usage
A = [2, 4, 1, 3, 2]
print(min_time_to_equal_elements(A))  # Output: 0
