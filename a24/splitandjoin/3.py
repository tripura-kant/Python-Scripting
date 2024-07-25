my_string = "python is a good language"

# nohtyp si a doog egaugnal

result = my_string.split()
print(result)

# for word in result:
#     res = word[::-1]
#     print(res, end=" ")

print(" ".join(word[::-1] for word in result))
