def sumofallsubarrays(arr, n):
    total = 0
    for s in range(n):
        for e in range(s, n):
            currentsum = 0
            for e in range(s, e+1):
                currentsum  += arr[e]

            total += currentsum

    print(total)

arr = [4,3,7,6]
n = len(arr)
sumofallsubarrays(arr, n)