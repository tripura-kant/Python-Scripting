'''
start
end

1. start to end total of all numbers
2. start to end total of all number divisible by 7
'''
start = int(input("Enter num    "))
end = int(input("Enter num  "))

total = 0
for i in range(start, end + 1):
    total = total + i
print(total, end=" ")
