def minimum_cost_to_remove_all_elements(A):
    # Handle the edge case when the array is empty
    if not A:
        return 0

    # Sort the array in descending order
    A.sort(reverse=True)

    # Initialize total cost and current total sum of the array
    total_cost = 0
    current_sum = sum(A)

    # Calculate the cost of removing elements
    for value in A:
        total_cost += current_sum
        current_sum -= value

    return total_cost


# Example usage
A1 = [2, 1]
A2 = [5]
print(minimum_cost_to_remove_all_elements(A1))  # Output: 4
print(minimum_cost_to_remove_all_elements(A2))  # Output: 5
