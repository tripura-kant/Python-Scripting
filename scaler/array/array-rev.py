# print(arr[::-1])

def rev_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1

    return arr


arr = [1, 3, 2, 9, 0]
print(rev_array(arr))
