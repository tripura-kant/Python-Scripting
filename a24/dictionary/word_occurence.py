# Define a function named word_count that takes one argument, 'str'.
def word_count(str):
    # Create an empty dictionary named 'counts' to store word frequencies.
    counts = dict()

    # Split the input string 'str' into a list of words using spaces as separators and store it in the 'words' list.
    words = str.split()

    # Iterate through each word in the 'words' list.
    for word in words:
        # Check if the word is already in the 'counts' dictionary.
        if word in counts:
            # If the word is already in the dictionary, increment its frequency by 1.
            counts[word] += 1
        else:
            # If the word is not in the dictionary, add it to the dictionary with a frequency of 1.
            counts[word] = 1

    # Return the 'counts' dictionary, which contains word frequencies.
    return counts


# Call the word_count function with an input sentence and print the results.
print(word_count('the quick brown fox jumps over the lazy dog.'))
