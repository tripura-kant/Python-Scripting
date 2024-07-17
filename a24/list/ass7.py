my_list = [5, 6, 7, 8, 4, 4, 12]

my_list.extend([1, 20, 3])
# print(my_list)

print(my_list.count(4))

x = my_list.index(4)
print(x)
print(my_list.sort(reverse=True))
print(my_list.sort(reverse=False))
print(my_list)
