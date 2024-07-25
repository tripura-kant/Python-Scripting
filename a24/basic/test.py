def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        largest = num1
    elif num2 > num1 and num2 > num3:
        largest = num2
    else:
        largest = num3
    print(f"{largest}")


num1 = input("Enter num ")
num2 = input("Enter num ")
num3 = input("Enter num ")
largest(num1, num2, num3)
