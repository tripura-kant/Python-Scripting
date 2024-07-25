def longest_word(s: str) -> str:
    current = ""
    longest = ""

    for char in my_string:
        if char == " ":
            if len(current) > len(longest):
                longest = current
            current = ""
        else:
            current += char

    if len(current) > len(longest):
        longest = current
    return longest


my_string = "Python is very easy language to learn"

print(longest_word(my_string))
