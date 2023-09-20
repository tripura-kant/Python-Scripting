# Cristiano is from Portugal and Messi is from Argentina.
# Cristiano plays for Al-Nassr and Messi plays for PSG.

# Find the count of occurrence of each unique word in the string
# E.g {“Cristiano”: 2, “Portugal”: 1, “Messi”: 2,  …….}

string = """Cristiano is from Portugal and Messi is from Argentina.
Cristiano plays for Al-Nassr and Messi plays for PSG """

words = string.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)