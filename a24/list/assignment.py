# my_list = [4, 8, 6, 5, 3, 12, 1, 3]
#
# n = len(my_list)
# total = 0
# for i in range(1, n):
#     if my_list[i] % 2 != 0:
#         total += 1
#         # print(total)
#
# print(f"Total odd numbers = {total}")

my_list = [4, 8, 6, 5, 3, 12, 1, 3, 6]

n = len(my_list)
even = 0
odd = 0
for i in range(1, n):
    if my_list[i] % 2 != 0:
        odd += 1
        # print(total
    else:
        even += 1

print(f"Total odd numbers = {odd}")
print(f"Total even numbers = {even}")
