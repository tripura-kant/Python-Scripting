# Second largest
def find_second_largest(arr):
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")
    n = len(arr)

    for i in range(0, n):
        if arr[i] > large:
            large = arr[i]

    for i in range(0, n):
        if arr[i] < small:
            small = arr[i]

    for i in range(0, n):
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    for i in range(0, n):
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    #     large = max(large, arr[i])
    #     small = min(small, arr[i])
    return large, small


arr = [1, 2, 3, 4, 5]
print(find_second_largest(arr))
