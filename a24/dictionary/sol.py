def word_count(str):
    count = {}

    words = str.split()
    # print(words)

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


print(word_count('the quick brown fox jumps over the lazy dog.'))
