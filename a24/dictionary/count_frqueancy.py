my_list = [4, 5, 3, 4, 1, 9, 2, 4, 9, 2, 7, 8, 3, 6, 8, 7, 9]
'''
4: 3


'''
result = {}

for num in my_list:
    if num in result:
        result[num] = result[num] + 1
    else:
        result[num] = 1

print(result)
