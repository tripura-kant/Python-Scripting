def solve(A):
    ans = 0
    n = len(A)
    for i in range(n):
        if A[i] == 'A':
            for j in range(i + 1, n):
                if A[j] == 'G':
                    ans += 1
    return ans


A = "GABG"
print(solve(A))
