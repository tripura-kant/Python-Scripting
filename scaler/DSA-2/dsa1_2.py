def prime(n):
    i = 1
    cnt = 0
    while i * i <= n:
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
        i += 1
    return (cnt == 2)


n = 14
print(prime(n))
