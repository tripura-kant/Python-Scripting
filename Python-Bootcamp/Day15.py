# Coffee machine project
import sys

water = 100
milk = 50
coffee = 76
money = 2.5

answer = input("What would you like? (espresso/latte/cappuccino):    ").lower()

if answer == "off":
    print("Turning off the machine...!!")
    sys.exit();
elif answer == "report":
    print("\nCurrent Resource Levels:")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}\n")
else:
    print(f"You chose {answer}")

#print(f" You choosed {answer}")

    print(print("\nCurrent Resource Levels:")
    print(print(f"Water: {water}ml")
    print(print(f"Milk: {milk}ml")
    print(print(f"Coffee: {coffee}g")
    print(print(f"Money: ${money}\n")