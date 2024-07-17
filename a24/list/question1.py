"""
Ask no from user = 6

Enter element = 2
Enter element = 2
Enter element = 2
Enter element = 2
Enter element = 2
Enter element = 2

[2,2,2,2,2,2]
"""
n = int(input("Enter no: "))

input_list = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    input_list.append(num)

print(input_list)
