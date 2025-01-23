def count_ag(s):
    count_of_pair = 0
    count_of_g = 0
    n = len(s)

    for char in reversed(s):
        if char == 'g':
            count_of_g += 1
        elif char == 'a':
            count_of_pair += count_of_g

    return count_of_pair

test_string = "abegegaga"
result = count_ag(test_string)
print(result)
