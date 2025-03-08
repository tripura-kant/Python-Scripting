# Noble Integer
arr = [2, 3, 4, 4, 4, 6, 4, 1, 2, 3]


def noble_number(arr):
    arr.sort()
    less = 0
    ans = 0

    for i in range(len(arr)):
        if arr[i] != arr[i - 1]:
            less = i
        if less == arr[i]:
            ans += 1

    print(ans)


noble_number(arr)
