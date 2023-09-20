# Write a Python function that accepts a string and calculates the number of uppercase and lowercase

def up_low(s):
    lowercase = 0
    uppercase = 0


    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'String: {s}')
    print(f'Lowercase count: {lowercase}')
    print(f'Uppercase count: {uppercase}')
s = 'Hello Mr. Rogers , how are you this fine Thisday'
up_low(s)
