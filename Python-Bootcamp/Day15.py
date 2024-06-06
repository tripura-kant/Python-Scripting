# Coffee machine project
import sys
answer = input("What would you like? (espresso/latte/cappuccino):    ").lower



if answer == "off":
    print("Turning off the machine...!!")
    sys.exit();

print(f" You choosed {answer}")