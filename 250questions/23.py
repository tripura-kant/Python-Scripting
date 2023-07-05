# Implement the hasDuplicates function which verifies if a list has duplicate values.

def hasDuplicates(list):
    flag = 0
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i] == list[j]):
                flag = 1
    if (flag == 1):
        return True
    else:
        return False


list = [1, 2, 3, 4, 4, 5, 6]

print(hasDuplicates(list))
