n = 24
# i = 1
# cnt = 0
# while i * i <= n:
#     if n % i == 0:
#         cnt += 1
#         if i != n // i:
#             cnt += 1
#     i += 1
# print(cnt)
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print(count)
