# def pattern_2(n: int):
#     for _ in range(n):
#         for _ in range(5):
#             print(1, end=" ")
#         print()
#
#
# # pattern(5)
# pattern_2(3)

# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(5, 0, -1):
#             print(j, end=" ")
#         print()
#
#
# pattern(5)

def pattern(n: int, m: int):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(j, end=" ")
        print()


pattern(5, 5)
