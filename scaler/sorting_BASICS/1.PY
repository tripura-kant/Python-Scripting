count = 0
for i in range(n):
    count_sum = 0
    for j in range(n):
        if arr[i] > arr[j]:
            count_sum += 1

        if count_sum == arr[i]:
            count += 1
