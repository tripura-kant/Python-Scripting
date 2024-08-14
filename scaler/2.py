    ''' m1,m2,m3,m4,m5= marks of the five subjects
    Output: Print percentage and the grade'''

# YOUR CODE GOES HERE
m1 = int(input("Enter num  "))
m2 = int(input("Enter num  "))
m3 = int(input("Enter num  "))
m4 = int(input("Enter num  "))
m5 = int(input("Enter num  "))

percentage = int(m1 + m2 + m3 + m4 + m5 / 5)
print(percentage)

if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
elif percentage >= 40:
    print("E")
else:
    print("F")
