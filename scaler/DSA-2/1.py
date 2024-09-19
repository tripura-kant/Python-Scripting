# Find sum of all subarray sums
def subarray_sums(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += arr[k]
            total += sum

    return total


arr = [1, 2, 3]
print(subarray_sums(arr))
