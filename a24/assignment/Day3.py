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
#     i += 1


def countDivisibleBy3And5(a: int, b: int) -> int:
    if a > b:
        a, b = b, a  # Ensure a is less than or equal to b
    count = 0
    current = a
    while current <= b:
        if current % 3 == 0 and current % 5 == 0:
            count += 1
        current += 1
    return count


print(countDivisibleBy3And5(100, -100))
