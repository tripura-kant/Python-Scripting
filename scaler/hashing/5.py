def largest_non_repeating_substring(s):
    start = 0
    end = 0
    hs = set()
    ans = 0

    while end < len(s):
        # If the character is already in the set, we need to move the start pointer
        while s[end] in hs:
            hs.remove(s[start])
            start += 1

        # Add the current character to the set
        hs.add(s[end])
        end += 1

        # Update the maximum length found
        ans = max(ans, end - start)

    return ans


# Example usage
s = "abcabcbb"
print(largest_non_repeating_substring(s))  # Output: 3
