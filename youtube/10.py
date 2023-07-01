# Step 1: Initialize an empty dictionary
word_counts = {}

# Step 2: Split the string into words
string = "Cristiano is from Portugal and Messi is from Argentina. Cristiano plays for Al-Nassr and Messi plays for PSG."
words = string.split()
# print(words)
# print('#########')
# Step 3: Update the dictionary with word counts
for word in words:
    # Check if the word is already present in the dictionary
    if word in word_counts:
        # If it is, increment the count by 1
        word_counts[word] += 1
    else:
        # If it is not, add the word to the dictionary with a count of 1
        word_counts[word] = 1

# Step 4: Print the resulting dictionary
print(word_counts)
