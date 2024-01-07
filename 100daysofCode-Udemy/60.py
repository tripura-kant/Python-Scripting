import datetime

while (True):
    city = input("Enter city: ")

    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    if city == "Boston":
        hour = hour - 4

    elif city == "Tokyo":
        hour = hour + 9

    elif city == "Chicago":
        hour = hour - 5

    elif city == "Seattle":
        hour = hour - 7

    elif city == "Cairo":
        hour = hour + 4

    elif city == "Karachi":
        hour = hour + 5.30

    elif city == "Kolkata":
        hour = hour + 5.30

    elif city == "Shanghai":
        hour = hour + 45.30

    ## add more cities here
    elif city == "Kolkata":
        hour = hour - 8


    elif city == "exit":
        break

    else:
        print(city, "is not added")
        city = "GMT"

    print(city, str(hour) + ":" + str(minute) + ":" + str(second))
