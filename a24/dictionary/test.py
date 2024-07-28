my_string = "the quick brown fox jumps over the lazy dog"
my_string1 = my_string.split()

result = {}
for word in my_string1:
    result[word] = result.get(word, 0) + 1

print(result)
