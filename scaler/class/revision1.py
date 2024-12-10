n = 6
i = 2
cnt = 0
while (i * i <= n):
    if n % i == 0:
        print(False)
    i += 1

print(n >= 2)
