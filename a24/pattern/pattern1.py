'''
1
12
123
1234
12345
'''

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#
#
# pattern(5)

# i = 5 j= 1      6-5+1 1
# i 4 j 2         6-4+1 2
# i 3 j 3

for i in range(5, 0, -1):
    for j in range(1, 6 - i + 1):
        print(j, end=" ")
    print()
