attempts = 0
attemts_max = 5

def login(name, num):
    user = input("your name is: ").lower()
    pin = int(input("enter pin: "))

    if user == name and pin == num:
        return True
    return False
while True:
    if login("monu",123):
        print("Login successful")
        break
    attempts += 1
    if attempts >= attemts_max:
        print("login failed")
        break
    print("Either pin or name not recognized, try again \n")        