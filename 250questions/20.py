# This is file 20.py

# Create a findMaximum function that receives a list as a parameter and returns the maximum value in the list.
# As you iterate over the list, you may want to keep track of the current maximum value in order to keep comparing it with
# the next elements of the list.

def findMaximum(l):
    maximum = 0
    index = 0
    for i, num in enumerate(l):
        if num > maximum:
            maximum = num
            index = i
    return [index, maximum]


l = [5, 2, 9, 1, 7]
print(findMaximum(l))
