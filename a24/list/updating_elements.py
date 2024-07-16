my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]
# print(my_list)
#
# my_list[-1] = 200
# print(my_list)

n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 1
    else:
        my_list[i] = my_list[i] - 1

print(my_list)
