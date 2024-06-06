# Coffee machine project
machine_state = on
answer = input("What would you like? (espresso/latte/cappuccino).lower:    ")

if answer == "off":
    machine_state = turn_off