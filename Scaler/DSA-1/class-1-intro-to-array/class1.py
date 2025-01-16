# Reverse array in python
arr = [1, 2, 3, 4, 5]


def rev_array(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    print(arr)


rev_array(arr)
