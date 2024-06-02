# Example usage:
num1 = 200
num2 = 33
num3 = 500

if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3

print("The greatest number among", num1, ",", num2, "and", num3, "is:", greatest)
