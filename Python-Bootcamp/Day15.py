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

print(f" You choosed {answer}")

if answer == "report":
