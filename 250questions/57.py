n = int(input())

if n % 2 == 0 and range(2, 6):
    print("Not Weird")
elif n % 2 == 0 and range(6, 21):
    print("Weird")
elif n % 2 == 0 and n > (101):
    print("Not Weird")
else:
    print("Weird")
