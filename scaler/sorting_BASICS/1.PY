# count = 0
# for i in range(n):
#     count_sum = 0
#     for j in range(n):
#         if arr[i] > arr[j]:
#             count_sum += 1
#
#         if count_sum == arr[i]:
#             count += 1

def count_noble_integers(arr):
    n = len(arr)
    count = 0

    # Handle the edge case of an empty array
    if n == 0:
        return count

    for i in range(n):
        count_sum = 0
        for j in range(n):
            if arr[i] > arr[j]:
                count_sum += 1

        if count_sum == arr[i]:
            # Ensure it's not a duplicate value that has already been counted
            # For example, if arr = [3, 3, 3, 5], the value 3 shouldn't be counted multiple times.
            if i == 0 or arr[i] != arr[i - 1]:
                count += 1

    return count


# Example usage
arr = [1, 1, 3, 3]
print(count_noble_integers(arr))  # Output should be 1
