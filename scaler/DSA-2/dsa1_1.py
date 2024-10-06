def factor(n):
    i = 1
    cnt = 0
    while i * i <= n:
        if n % i == 0:
            cnt += 1  # Count the divisor
            if i != n // i:  # Only add the corresponding factor if it's different
                cnt += 1  # Count the corresponding factor
        i += 1
    return cnt


n = 100
print(factor(n))  # Should return 9
