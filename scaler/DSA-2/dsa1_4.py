n = 7
arr = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4
arr1 = arr[n - k:]
print(arr1)
for i in range(n - k):
    arr1.append(arr[i])
print(arr1)
