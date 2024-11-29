arr = [-4, 5, 2, 1, 6]

n = len(arr)
ans = -100
s = 0
for i in range(n):
    for j in range(i, n):
        s = 0
        for k in range(i, j + 1):
            s += arr[k]
        ans = max(ans, s)
print(ans)
