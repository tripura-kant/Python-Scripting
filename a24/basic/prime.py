def count_factors(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    return count


def check_prime(n):
    factors = count_factors(n)
    if factors == 2:
        return True
    return False


print(check_prime(17))
print(check_prime(27))
