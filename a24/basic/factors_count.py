def factors(num):
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    print(count)


factors(20)

# print(555 // 2)
