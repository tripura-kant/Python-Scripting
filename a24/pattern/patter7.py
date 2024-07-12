'''
                *
             * * *
             * * * *
            * * * * *
'''
n = 5
for i in range(n // 2, 0, -1):
    for j in range(1, 5 - i + 1):
        print(" ")
    for k in range(i, i * 2):
        print(k, end=" ")
