# i = 1
# while i <= 10:
#     print(i, end="")
#     i += 1
# print()
# # print(i)
#
# num = int(input("Enter no "))
# i = 1
# while i <= num:
#     print(i, end=" ")
# #     i += 1
#
#
# def countDivisibleBy3And5(a: int, b: int) -> int:
#     # if a > b:
#     #     a, b = b, a  # Ensure a is less than or equal to b
#     count = 0
#     current = a
#     while current <= b:
#         if current % 3 == 0 and current % 5 == 0:
#             count += 1
#         current += 1
#     return count
#
#
# print(countDivisibleBy3And5(3, 50))
# n = 5
# i = 1
#
# while i < 11:
#     print(n * i)
#     i += 1
#     # print(sum)
n = 23


def sum_of_square(n):
    i = 1
    sum = 0
    while i <= n:
        x = i ** 2
        sum += x
        i += 1
    print(sum)


sum_of_square(n)
