# Write a function that takes a string and return it reversed.

def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

my_string = "abc"
print(reverse_string(my_string))