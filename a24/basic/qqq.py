# n = int(input("enter num    "))


#
#
# def total_cups(n):
#     result = n // 6
#     final = n + result
#     print(int(final))
#
#
# total_cups(6)
# def pattern(n):
#     i = 1
#     while i <= n:
#         result = i * 10
#         print(result)
#         i += 1
#
#
# pattern(2)

# def pattern(n):
#     i = 0
#     while i < n:
#         result = 2 ** i
#         print(result)
#         i += 1
#
#
# pattern(7)

# def pattern(n: int) -> None:
#     num = 1
#     i = 1
#     while i <= n:
#         print(num)
#         num = (num * 10) + 1
#         i += 1
#
#
# pattern(5)

# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(1, 6):
#             print(1, end=" ")
#         print()
#
#
# # Alternate Way
# def pattern_2(n: int):
#     for _ in range(n):
#         for _ in range(5):
#             print(1, end=" ")
#         print()
#
#
# pattern(3)
# # pattern_2(3)

def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(5, 0, -1):
            print(j, end=" ")
        print()


pattern(5)
