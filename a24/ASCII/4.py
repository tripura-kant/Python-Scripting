'''
    enter untill q button pressed
'''

my_string = ""
while True:
    char = input("Enter string  ")
    if char == "q" or char == "Q":
        break
    my_string += char

print(my_string)
