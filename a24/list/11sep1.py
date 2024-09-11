# def largest(arr):
#     arr.sort()
#     print(arr)
#     return arr[-1]
#
#
# arr = [1, 8, 7, 56, 90]
#
# print(largest(arr))

def largest(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


arr = [1, 8, 7, 56, 90]

print(largest(arr))
