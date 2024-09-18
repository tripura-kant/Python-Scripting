# Find sum of all subarray sums

for i in range(n):
    for j in range(i, n):
        sum = 0
        for k in range(i, j + 1):
            sum += arr[k]
           