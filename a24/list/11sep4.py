# check if array is sorted

def check_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


arr = [1, 2, 3, 4, 5, 6]
print(check_sort(arr))
