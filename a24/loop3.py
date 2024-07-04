i = int(input("Enter num1 "))  # 9
j = int(input("Enter num2 "))  # 3

if i > j:
    start = j
    end = i
else:
    start = i
    end = j

current_number = start
while current_number <= end:
    print(current_number, end=" ")
    current_number = current_number + 1
