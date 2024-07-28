# def pattern(n: int) -> None:
#     i = 0
#     while i < n:
#         print(2 ** i)
#         i += 1
#
#
# pattern(7)

n = 5


# def pattern(n):
#     i = 1
#     while i < n + 1:
#         print(i ** 2)
#         i += 1
#
#
# pattern(n)

# def pattern(n: int) -> None:
#     num = 2
#     i = 1
#     while i <= n:
#         print(num)
#         num = (num * 10) + 2
#         i += 1
#
#
# pattern(5)

def harmonic_series(n: int) -> float:
    sum_harmonic = 0.0
    i = 1
    while i <= n:
        sum_harmonic += 1 / i
        i += 1
    # Round is a new function I have not taught yet, google it
    return round(sum_harmonic, 2)


print(harmonic_series(14))
