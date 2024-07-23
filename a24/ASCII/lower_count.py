my_string = "asdasdasdasdskjhd*()&(*^*&%&^$"

count = 0
count1 = 0
# for ch in my_string:
#     ascii_code = ord(ch)
#     if 97 <= ascii_code <= 122:
#         count += 1
#
# print(f"Total lowercase letters = {count}")

my_string = "ExampleString123"

count_lower = 0
count_upper = 0

for ch in my_string:
    if 'a' <= ch <= 'z':  # Check if character is lowercase
        count_lower += 1
    elif 'A' <= ch <= 'Z':  # Check if character is uppercase
        count_upper += 1

print(f"Total lowercase letters = {count_lower}")
print(f"Total uppercase letters = {count_upper}")
