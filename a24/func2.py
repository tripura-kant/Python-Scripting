def func(base, power):
    if power == 0:
        return 1
    return base * func(base, power - 1)


x = func(5, 3)
print(x)
