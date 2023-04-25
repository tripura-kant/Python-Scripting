# Exercise: Check for duplicate in list

some_list = ['a', 'b', 'c', 'd', 'm', 'n', 'c', 'n']

duplicate = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
           duplicate.append(value)

print(duplicate)
