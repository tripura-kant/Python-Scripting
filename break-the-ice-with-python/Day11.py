# number = float(input("Enter a number: "))

# if number > 10:
#     print("Number is greater than 10")
# elif number < 10:
#     print("Number is less than 10")
# else:
#     print("Number is equal to 10")

#Python Program to check largest number among three numbers


num1 = float(input("Enter a num1: "))
num2 = float(input("Enter a num2: "))
num3 = float(input("Enter a num3: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3   

print("The largest number is {0}".format(largest))