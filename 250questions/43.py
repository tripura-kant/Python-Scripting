# This is file 43.py
# Exception HANDLING

try:
    a = int(input("Enter your number "))
    print(a + 3)

except Exception as e:
    print('some error occured', e)
