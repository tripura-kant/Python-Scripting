#
# UPPERCASE > LOWERCASE
# LOWERCASE > UPPERCASE


my_string = "sdasD dsfsfdsDADASD"

result = ""

for ch in my_string:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        ascii_code += 32
        result = result + chr(ascii_code)
    else:
        ascii_code -= 32
        result = result + chr(ascii_code)

print(result)
