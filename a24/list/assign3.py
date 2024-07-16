my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


for num in my_list:
    if is_prime(num):
        print(num, end=" ")
