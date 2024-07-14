# sum of all even number
my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

n = len(my_list)
sum = 0
for i in my_list:
    if i % 2 == 0:
        sum = sum + i
        # print(i)

print(sum)

n = len(my_list)
sum = 0
for i in range(0, n):
    if my_list[i] % 2 == 0:
        sum = sum + my_list[i]
        # print(my_list[i])

print(sum)
