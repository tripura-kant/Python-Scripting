def func(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return func(arr, start + 1, end - 1)


arr = [2, 3, 5, 6, 3]
result = func(arr, 0, len(arr) - 1)
print(result)
