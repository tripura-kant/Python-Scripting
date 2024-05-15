# print("Welcome to roalacoaster")
# height = int(input("What is your height in cm "))
#
# if height >= 120:
#     print("You can ride the roalacoaster")
# else:
#     print("You cannot ride")


# Execrcise
#
# numbers=int(input("Enter no "))
#
# if numbers % 2 == 0:
#     print("EVEN")
# else:
#     print("ODD")
#Multiple if else

height = input("Enter heght")
bill = 0

if height >=120:
    print("You can ride the roalacoster")
    age = int("What is your age? ")
    if age < 12:
        bill = 5
        print("Child ticket worth $5")
    elif age < 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Your ticket is $12 ")

    wants_photo = input("Do you want a photo taken ? Y OR N")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("")