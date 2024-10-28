def binary_search(arr, k):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] < k:
            l = mid + 1
        elif arr[mid] > k:
            h = mid - 1
        else:
            return mid


arr = [2, 3, 4, 5, 6, 6, 7, 21, 2, 1]

k = 5

print(binary_search(arr, k))
