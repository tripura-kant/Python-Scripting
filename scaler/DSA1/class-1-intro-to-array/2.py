# Reverse array from start and end range

arr = [1, 2, 3, 4, 5]
start = 1
end = 3


# output arr = [1,4,3,2,5]

def rev_array(arr, start, end):
    n = len(arr)
    i = start
    j = end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    print(arr)


rev_array(arr, start, end)
