# n = int(input("Enter no of subject "))
#
# result = {}
# for i in range(n):
#     sub = input("enter subject")
#     marks = input("Enter marks")
#     result[sub] = marks
#
# formatted_result = {f"{key}": f"{value}" for key, value in result.items()}
# print(formatted_result)


my_list = [4, 5, 3, 4, 1, 9, 2, 4, 9, 2, 7, 8, 3, 6, 8, 7, 9]

result = {}

for num in my_list:
    result[num] = result.get(num, 0) + 1

max_freq = 1
max_num = 1
for num, freq in result.items():
    # print(num, freq)
    if freq > max_freq:
        max_freq = freq
        max_num = num
print(f"{max_num} (Frequency: {max_freq})")
# print(result)
