def count_noble_integers(arr):
    n = len(arr)
    count = 0

    # Edge case: if the array is empty
    if n == 0:
        return count

    # Sort the array
    arr.sort()

    # Iterate through the3.py
    # sorted array
    for i in range(n):
        # Count of elements greater than arr[i]
        count_greater = n - i - 1

        # Check if arr[i] is a noble integer
        # Ensure it's not a duplicate value that has already been counted
        if arr[i] == count_greater:
            # Ensure it's not a duplicate value that has already been counted
            if i == n - 1 or arr[i] != arr[i + 1]:
                count += 1

    return count


# Example usage
arr = [1, 1, 3, 3]
print(count_noble_integers(arr))  # Output should be 1
