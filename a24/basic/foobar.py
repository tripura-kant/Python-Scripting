'''
Ask a number from user
if num devisible by 3 -- > FOO
if num devisible by 5 -- > FOO
if num devisible by 8 -- > FOO
if num devisible by 3 -- > FOO
'''

num = int(input("Enter a number "))

if num % 3 == 0 and not num % 5 == 0:
    print("Foo")
elif num % 5 == 0 and not num % 5 == 0:
    print("bar")
elif num % 5 == 0 and num % 3 == 0:
    print("FoodBar")
else:
    print("Invalid")
