# n = 4
# i = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# n = 4
# i = 1
# for i in range(1, n + 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# # Q3
# n = 5
# i = 1
# for i in range(n, 0, -1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

# # Q4
# n = 5
# for i in range(n, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

# # Q5
# n = 5
# for i in range(1, n + 1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()


# # Q6
# n = 6
# for i in range(1, n + 1):
#     for j in range(i, 6):
#         print(j, end=" ")
#     print()

# # Q7
# n = 5
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# # Q8
# n = 5
# num = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#     print()

# 9
# def pattern(n: int):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             if j % 2 == 0:
#                 print(2, end=" ")
#             else:
#                 print(1, end=" ")
#         print()
#
#
# pattern(5)

# Q10
# def pattern(n: int):
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#
#
# pattern(5)

a = 1
b = 30


def countdiv(a, b):
    if a > b:
        a, b = b, a
    count = 0
    current = a
    while current <= b:
        if current % 3 == 0 and current % 5 == 0:
            count += 1
        current += 1
    return count


print(countdiv(a, b))
