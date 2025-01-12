# Rotate k times array
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)


def rotate(arr, n, k):
    for i in range(k):  # rotate k times
        temp = arr[n - 1]  # last element
        for j in range(n - 1, 0, -1):
            arr[j] = arr[j - 1]
        arr[0] = temp


rotate(arr, n, k)
print(arr)
