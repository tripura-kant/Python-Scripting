# Print all prime number
my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

n = len(my_list)
total = 0


# factor = 0
def is_prime(num):
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor += 1
    if factor == 2:
        return True


for index in range(0, n):
    if is_prime(my_list[index]) == True:
        print(my_list[index])
