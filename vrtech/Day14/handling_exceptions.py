try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ZeroDivisionError:
    print("Value cant be zero")
except ValueError:
    print("Must provide value")
