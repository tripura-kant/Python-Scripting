# sum of all even number
my_list = [5, 34, 98, 21, 29, 2]

n = len(my_list)
sum = 0
for i in range(0, n):
    if i % 2 == 0:
        sum = sum + my_list[i]

print(sum)
