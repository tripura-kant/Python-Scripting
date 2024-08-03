# x = 55
#
#
# def hi():
#     return x
#
#
# x += 10
# print(hi())
#
# Iterate to find all the factors of given number n from 1 to (n // 2) + 1, the number would have no factors beyond this.
# A number is the factor of n if it completely divides it without any remainder.
# Take the sum of all factors of the given number n.

def perfect_number(n):
    if n <= 1:
        return 0
    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == n:
        return 1
    else:
        return 0


print(perfect_number(6))
