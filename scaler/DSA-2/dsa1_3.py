def prime(n):
    i = 2
    cnt = 0
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 10
print(prime(n))
