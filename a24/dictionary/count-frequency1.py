my_list = [4, 5, 3, 4, 1, 9, 2, 4, 9, 2, 7, 8, 3, 6, 8, 7, 9]
'''
4: 3


'''
my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
