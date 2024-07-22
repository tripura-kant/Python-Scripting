# Member not in/in
my_list = [3, 6, 7, 5, 6]
# print(6 in my_list)
result = []

for num in my_list:
    if num not in result:
        result.append(num)

print(result)
