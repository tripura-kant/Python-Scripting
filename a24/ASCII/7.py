'''
remove all symbol,digits, spaces from string
'''

my_string = "a%b@cadasd12_"

result = ""

# for ch in my_string:
#     if "a" <= ch <= "z":
#         result += ch
#
# print(result)

for ch in my_string:
    if ord("a") <= ord(ch) <= ord("z"):
        result += ch

print(result)
