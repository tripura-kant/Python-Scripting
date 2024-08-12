def set_operation(sent1, sent2):
    words1 = sent1.split()
    words2 = sent2.split()
    print(words1)
    print(words2)

    a = set(words1)
    b = set(words2)

    total_unique_count = len(a) + len(b)

    return total_unique_count


# Example usage
sentence1 = "in data analysis we use data and process it further to create better interpreted data"
sentence2 = "more and more data will be passively collected"

# Get result
total_unique_count = set_operation(sentence1, sentence2)

# Print result
print(f"{total_unique_count}")
