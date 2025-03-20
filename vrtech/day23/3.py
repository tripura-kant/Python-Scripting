from functools import reduce


def add(x, y):
    return x + y


mylist = [1, 2, 3, 4, 5]

print(reduce(add, mylist))
