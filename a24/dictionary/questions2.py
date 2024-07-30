my_string = "asdasdadqoiwdsajkssshfkjgakshdlkajsldhas"

my_dict = {}
max = 0
max_element = 0
for num in my_string:
    my_dict[num] = my_dict.get(num, 0) + 1

for key in my_dict:
    if my_dict[key] > max:
        max = my_dict[key]
        max_element = key

print(my_dict)
# print(max)
# print(max_element)
print(f"Maximum element is {max_element} and max key is {max}")
