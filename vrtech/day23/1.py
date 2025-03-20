mylist = [1, 2, 3, 4]


def square(x):
    return x * x


# mynewlist = list(map(square, mylist))
# print(mynewlist)

# new_list = []
# for each in my_list:
#     new_list.append(each * each)
#
# print(new_list)
# mynewlist = list(map(square, mylist))
# print(mynewlist)
mynewlist = list(map(int, mylist))
print(mynewlist)
