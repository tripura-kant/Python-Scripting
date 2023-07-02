# This is file 7.py
# Cube of number between 1 to 21


def getCube():
    li = [x * x * x for x in range(1, 21)]
    return li


li = getCube()
print(li)
