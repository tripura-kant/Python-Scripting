# Write a Python function to multiply all the numbers in a list


def multiply_num(numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total


s = multiply_num([1, 2, 3, 4])
print(s)
