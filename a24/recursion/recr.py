def func(num):
    if num == 1:
        return 1
    return num * func(num - 1)


x = func(0)
print(x)
