"""

1. Take 10 integer inputs from user and store them in a list. Now, copy all
the elements in another list but in reverse order.

"""
input_list = []
for i in range(3):
    num = int(input(f"Enter num {i + 1}:  "))
    input_list.append(num)

print(input_list)
input2 = input_list[::-1]
print(input2)
input_list.reverse()
print(input_list)
