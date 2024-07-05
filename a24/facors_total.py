'''
368 factor ke total
'''


def factor(num):
    i = 1
    total = 0
    while i <= num:
        if num % i == 0:
            # total = total + i
            # print(i, end=" ")
            total = total + i
            # print(total)
        i += 1
    print(total)
    # return total


factor(368)
