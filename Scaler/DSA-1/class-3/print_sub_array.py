def print_sub_array(arr, start, end):
    for i in range(start, end+1):
        print(arr[i], end =' ')
    print()



arr = [1, 2, 3, 4, 5, 6]
start = 0
end = 2
print_sub_array(arr, start, end)

