def print_all_sub_array(arr, n):
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end=" ")
            print()

arr = [1,2,3,4]
n = len(arr)
print(print_all_sub_array(arr,n))