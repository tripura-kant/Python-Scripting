# sum of odd index elements
my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

n = len(my_list)
total = 0

for i in range(0, n):
    if i % 2 != 0:
        total = total + my_list[i]
        # print(my_list[i])

print(total)
