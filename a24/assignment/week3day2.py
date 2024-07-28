# n = 5
#
# for i in range(1, n + 1):
#     for j in range(i, i + 1):
#         print(j, end="")
#     print()


# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#
#
# pattern(4)

# q2
# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(i, 0, -1):
#             print(j, end=" ")
#         print()
#
#
# pattern(5)

# q3

def pattern(n: int):
    for i in range(5, 0, -1):
        for j in range(i, 6):
            print(j, end="")
        print()


pattern(5)
