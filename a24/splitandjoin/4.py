my_string = "python is a good language"

# nohtyp si a doog egaugnal

# egaugnal doog a si nohtyp


result = my_string.split()
# print(result)

result.reverse()
# print(result)

for word in result:
    result = word[::-1]
    print(result, end=" ")

# print(" ".join(word[::-1] for word in result))
