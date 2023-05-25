# Prime number cChecker challenge


num = int(input("Enter a number: "))

if num == 1:
    print("1 is not prime")

elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not prime")
            print(i, "times", num//i, "is", num)
            break 
        else:
            print(num, "is prime")
            
               