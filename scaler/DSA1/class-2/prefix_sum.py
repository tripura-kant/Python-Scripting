# Code for prefix sum

def prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n  # Initialize prefix sum to zero

    # First element of prefix sum should be same as original array
    prefix[0] = arr[0]

    # Calculate the prefix sum for the rest of array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


arr = [1, 2, 3, 4, 5]
prefix = prefix_sum(arr)
print(prefix)  # 1, 3, 6, 10, 15
