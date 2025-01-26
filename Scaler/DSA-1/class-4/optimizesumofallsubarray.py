def sumofallsubarrays(arr, n):
    total = 0
    for s in range(n):
        for e in range(s, n):
            subarraysum = 0
            for k in range(s, e+1):
                subarraysum  += arr[k]

            total += subarraysum

    print(total)

arr = [4,3,7,6]
n = len(arr)
sumofallsubarrays(arr, n)