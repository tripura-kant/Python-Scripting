"""
Cristiano is from Portugal and Messi is from Argentina.
Cristiano plays for Al-Nassr and Messi plays for PSG.

Find the count of occurrence of each unique word in the string
E.g {“Cristiano”: 2, “Portugal”: 1, “Messi”: 2,  …….}
"""
input_string = """Cristiano is from Portugal and Messi is from Argentina.
Cristiano plays for Al-Nassr and Messi plays for PSG."""

words = input_string.split()

# Initialize an empty dictionary to store word counts
word_counts = {}

# Iterate through each word in the list of words
for word in words:
    # Check if the word is already in the dictionary
    if word in word_counts:
        # Increment the count of the word if it's already in the dictionary
        word_counts[word] += 1
    else:
        # Add the word to the dictionary with initial count of 1 if it's not already in the dictionary
        word_counts[word] = 1

# Print the dictionary containing word counts
print(word_counts)
