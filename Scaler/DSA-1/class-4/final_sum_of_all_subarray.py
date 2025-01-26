def sum_of_subarray(A):
    ans = 0
    n = len(A)
    for i in range(n):
        ans += A[i] * (i + 1) * (n-1)

    print(ans)

A = [4,5,1,2]
sum_of_subarray(A)