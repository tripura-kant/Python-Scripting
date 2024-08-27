def has_good_pair(A, B):
    seen = set()

    for num in A:
        complement = B - num
        if complement in seen:
            return True
        seen.add(num)

    return False


# Example usage:
A = [1, 2, 3, 4, 5]
B = 9
print(has_good_pair(A, B))  # Output: True, because 4 + 5 = 9
