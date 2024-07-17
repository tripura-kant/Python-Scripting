my_list = [2, 3, 6, 8, 4, 9, 5, 7]
result = []

n = len(my_list)

for i in range(n):
    if my_list[i] % 2 != 0:
        result.append(my_list[i])

print(result)
