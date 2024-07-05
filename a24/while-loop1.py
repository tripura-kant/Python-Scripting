'''
Product of numbers 1*2*3...n
'''


def product_of_num(num):
    i = 1
    total = 1
    while i <= num:
        total = total * i
        i += 1
    return total


print(product_of_num(10))
