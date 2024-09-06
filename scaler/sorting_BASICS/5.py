def nobel_integer(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        if i == arr[i]:
            count += 1
    return count


# Example usage
arr = [1, 1, 3, 3]
print(nobel_integer(arr))  # Output should be
