# Args kargs

def super_func(*args):
    print(*args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, 6))
