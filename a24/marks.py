'''
 Ask marks from user

 91 - 100 A
'''

marks = int(input("Enter your marks "))

if marks >= 91 and marks <= 100:
    print("your grade is A")
elif marks >= 81 and marks <= 90:
    print("your grade is b")
elif marks >= 71 and marks <= 80:
    print("your grade is c")
elif marks >= 61 and marks <= 70:
    print("your grade is d")
elif marks >= 51 and marks <= 60:
    print("your grade is e")
else:
    print("fail")
