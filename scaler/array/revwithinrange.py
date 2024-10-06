def rev_array(arr):
    n = len(arr)
    i = 2
    j = 4

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


arr = [1, 3, 2, 9, 0]
print(rev_array(arr))
