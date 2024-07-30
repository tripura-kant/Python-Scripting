# find maximum frequency

my_list = [4, 5, 6, 3, 2, 4, 4, 4, 5, 4, 4, 4, 4, 3, 3, 9]

my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1

ans = 0
for key in my_dict:
    if my_dict[key] > ans:
        ans = my_dict[key]

print(ans)
