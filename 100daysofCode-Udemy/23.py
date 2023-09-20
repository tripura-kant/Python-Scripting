# Write a Python function that takes a list and returns a new list with unique elements of first list

def unique_list(lst):
    seen_num = []

    for number in lst:
        if number not in seen_num:
            seen_num.append(number)
    return seen_num


s = unique_list([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 6, 7, 8])
print(s)
