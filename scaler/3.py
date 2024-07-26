amount = int(input("Please enter amount "))
if amount >= 500 and amount % 100 == 0:
    print("Discharging amount")
else:
    if amount < 500 and amount % 200 == 0:
        print("Discharging amount")
    else:
        print("Not available")
